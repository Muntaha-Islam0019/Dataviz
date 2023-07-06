import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDateEdit, QPushButton
from PyQt5.QtCore import Qt, QDate
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime


class TemperatureGraphApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temperature Graph")
        self.layout = QVBoxLayout()

        # Date Range Selection
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setCalendarPopup(True)
        self.start_date_edit.setDate(QDate.currentDate().addDays(-7))  # Set initial date range
        self.layout.addWidget(QLabel("Start Date:"))
        self.layout.addWidget(self.start_date_edit)

        self.end_date_edit = QDateEdit()
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDate(QDate.currentDate())  # Set initial date range
        self.layout.addWidget(QLabel("End Date:"))
        self.layout.addWidget(self.end_date_edit)

        # Plot Button
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot_graph)
        self.layout.addWidget(self.plot_button)

        # Graph Canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

    def plot_graph(self):
        start_date = self.start_date_edit.date().toPyDate()
        end_date = self.end_date_edit.date().toPyDate()

        dates, temperatures = [], []

        with open('temperature_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                date_str = row['Date']
                temperature = float(row['Temperature'])
                date = datetime.strptime(date_str, '%Y-%m-%d').date()  # Convert string to date object
                if start_date <= date <= end_date:
                    dates.append(date_str)
                    temperatures.append(temperature)

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        ax.plot(dates, temperatures, 'b-')  # Line plot
        ax.scatter(dates, temperatures, color='red', marker='o')  # Scatter points

        ax.set_xlabel('Date')
        ax.set_ylabel('Temperature')

        ax.set_title('Temperature Graph')

        ax.grid(True)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TemperatureGraphApp()
    window.show()
    sys.exit(app.exec_())
