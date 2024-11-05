# Histogram Web Application

## Description
This project is a simple web application built with Shiny for Python, allowing users to upload a CSV file, select a specific column, and visualize the data in a histogram. The application provides an interactive interface to choose the column and adjust the number of histogram bins.

## Features
- Upload a CSV file with the dataset.
- Select a column from the uploaded CSV to visualize.
- Adjust the number of bins in the histogram.
- View data in a tabular format alongside the histogram plot.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Install the Required Libraries**: Ensure you have Python 3 installed, and then install the necessary packages: 
   ```bash
   pip install -r requirements.txt

## Usage
1. **Run the Application**: Start the Shiny application by executing:
   ```bash
   shiny run --reload --launch-browser app_hist.py

2. **Interacting with the App**:

- Upload a CSV file using the "Choose CSV File" option.
- Select the column to visualize from the dropdown menu.
- Choose the desired number of bins for the histogram.
- View the table data and histogram plot in the respective tabs.   

## File Structure
- `app_hist.py` : Main application file containing the web app code.

## Dependencies
- `pandas`
- `plotly`
- `shiny`
- `shinywidgets`
- `matplotlib`

This README provides a basic overview of the project, instructions for setup and use, and other relevant information. Let me know if there’s anything specific you’d like to add or modify. Feel free to contribute or reach out if you have any questions!


