# tempTrends
A repository containing code to analyze global temperature trends.

This project uses Taipy, a Python GUI framework, to visualize synthetic temperature trends over time, simulating global warming. The goal of this program is to provide an interactive chart that shows how the temperature on our planet has increased over a period of years. The user can interact with the program by adjusting a slider to change the range of years for the temperature trend. As the slider is adjusted, the temperature data and chart are dynamically updated, demonstrating how temperatures increase over time.

Features:

Temperature Simulation: The program simulates the rise in global temperatures using a simple linear model.
Interactive Slider: The user can adjust the slider to choose a year range and the chart updates accordingly.
Real-time Updates: The chart and data are updated in real time based on the user's interaction with the slider.
Graphical Representation: A dynamic chart visualizes the temperature trend, showing the relationship between the year and temperature.

Project Structure:

The code is organized into multiple files for modularity and readability...
config.py: Contains configuration settings such as the starting year, base temperature, and the trend factor for temperature change.
data.py: Contains the simulate_temperature_data function, which generates the synthetic temperature data for a given number of years.
gui.py: Contains the Taipy GUI setup, including the creation of the page, slider, chart, and dynamic updates when the slider changes.
main.py: The entry point for the program. It initializes the data, builds the GUI, and starts the application.
