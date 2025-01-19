from taipy.gui import Gui
from gui import build_gui
from data import simulate_temperature_data
from config import INITIAL_YEAR_RANGE

# Compute initial data based on starting range
years, temperatures = simulate_temperature_data(INITIAL_YEAR_RANGE)

# Set initial state for Taipy GUI
state = {"value": INITIAL_YEAR_RANGE, "years": years, "temperatures": temperatures}

# Build the GUI layout
page = build_gui()

# Run the Taipy GUI with the page layout
if __name__ == "__main__":
    Gui(page=page).run(title="Global Warming Temperature Trend")
