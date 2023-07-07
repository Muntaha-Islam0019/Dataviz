# Dataviz

## Overview

The Dataviz project is a PyQt5 application that allows users to visualize temperature data from a CSV file. It provides a graphical user interface (GUI) for selecting a date range and graph type, and displays the corresponding temperature graph using Matplotlib.

The main code provided implements the TemperatureGraphApp class, which extends the QWidget class from PyQt5. The class represents the main application window and contains all the necessary widgets and logic for data visualization.

## Requirements

To run the Dataviz project, ensure that you have the following dependencies installed:

- Python 3.x
- PyQt5
- Matplotlib

## Installation

1. Clone the GitHub repository for the Dataviz project using the following command:

   ```
   git clone https://github.com/your-username/your-repository.git
   ```

2. Change into the project directory:

   ```
   cd your-repository
   ```

3. Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Dataviz application, follow these steps:

1. Make sure you have a CSV file named "temperature_data.csv" in the project directory. The file should contain temperature data with columns "Date" and "Temperature".

2. Run the application by executing the main script:

   ```
   python main.py
   ```

3. The Temperature Graph window will open, displaying the following components:

   - **Start Date**: A date selection field for choosing the start date of the temperature data range.
   - **End Date**: A date selection field for choosing the end date of the temperature data range.
   - **Graph Type**: A dropdown menu for selecting the type of graph to display (Line Graph or Bar Graph).
   - **Plot**: A button that triggers the graph generation based on the selected options.
   - **Graph Canvas**: The area where the temperature graph will be displayed.

4. Select the desired start and end dates using the date selection fields.

5. Choose the graph type from the dropdown menu.

6. Click the **Plot** button to generate the temperature graph based on the selected options. The graph will be displayed in the Graph Canvas area.

7. To exit the application, close the Temperature Graph window.

## Code Explanation

The main code provided consists of a single class, `TemperatureGraphApp`, which represents the main application window. Here's an explanation of the key components:

- **Import Statements**: The necessary modules and classes are imported, including PyQt5, Matplotlib, and CSV.

- **TemperatureGraphApp Class**: This class extends the `QWidget` class from PyQt5 and represents the main application window. It contains the following components:
  - Date Range Selection: `QDateEdit` fields for selecting the start and end dates of the temperature data range.
  - Graph Type Selection: A `QComboBox` for choosing the type of graph to display.
  - Plot Button: A `QPushButton` that triggers the graph generation based on the selected options.
  - Graph Canvas: A `FigureCanvas` widget from Matplotlib for displaying the temperature graph.

- **plot_graph Method**: This method is called when the user clicks the Plot button. It retrieves the selected date range, reads the temperature data from the CSV file, filters the data based on the date range, and generates the temperature graph using Matplotlib. The type of graph (line graph or bar graph) is determined by the selected option from the dropdown menu.

- **Main Script**: The main script sets up the QApplication, creates an instance of the TemperatureGraphApp class, and starts the application event loop.

## Future Enhancements

Here are some possible enhancements for the Dataviz project:

- Improve error handling: Add appropriate error handling for cases such as missing CSV file or invalid data format.
- Implement data preprocessing: Add options to preprocess the temperature data, such as applying smoothing or filtering techniques.
- Add additional graph customization: Provide more options to customize the appearance of the temperature graph, such as axis labels, legends, and color schemes.
- Support multiple data sources: Extend the application to handle data from different sources, such as databases or web APIs.
- Export functionality: Allow users to export the generated graph as an image or save it to a file.

Feel free to implement any of these enhancements based on your project requirements.

## Conclusion

The Dataviz project provides a simple and intuitive way to visualize temperature data using a PyQt5 application. By following the provided documentation, you can easily set up and use the application to generate temperature graphs based on your data. Feel free to modify the code or enhance the application according to your specific needs. Happy data visualization!
