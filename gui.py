import taipy.gui.builder as tgb
from data import simulate_temperature_data

def on_slider(state):
    #This function updates the temperature data based on the slider's value.
    #It recalculates the data and updates the chart dynamically
    years, temps = simulate_temperature_data(state.value)
    state.years = years
    state.temperatures = temps

def build_gui():
    #Builds and returns the Taipy GUI layout for displaying temperature trends

    with tgb.Page() as page:
        tgb.text(value="# Global Temperature Trend Analysis", mode="md")  # Page title
        tgb.text(value="This simulation shows the temperature trends over time and how they are affected by global warming.")
        tgb.text(value="Adjust the slider to change the time range.")  # Slider instructions
        
        # Slider for selecting the number of years to display (50 to 200 years)
        tgb.slider(value="{value}", min=50, max=200, step=1, on_change=on_slider)
        
        # Chart for displaying the temperature data over time
        tgb.chart(data="{years, temperatures}", x_axis_label="Year", y_axis_label="Temperature (°C)")
        
        # Display the current year range dynamically
        tgb.text(value="Year range: {value} years")

    return page
