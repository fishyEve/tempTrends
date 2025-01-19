
from config import START_YEAR, BASE_TEMP, TREND_FACTOR

def simulate_temperature_data(years: int, trend_factor: float = TREND_FACTOR) -> tuple:
    #Generates synthetic temperature data with an increasing trend (simulating global warming).
    
    # years: The number of years to simulate.
    # trend_factor: A factor determining the rate of temperature increase (in Celsius since everyone else uses that).
    # returns tuple of two lists: years and temperatures.

    years_range = list(range(START_YEAR, START_YEAR + years)) 
    temperatures = [BASE_TEMP + trend_factor * (year - START_YEAR) for year in years_range]  # Linear growth model
    return years_range, temperatures
