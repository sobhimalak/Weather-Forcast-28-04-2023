import pandas as pd
import matplotlib.pyplot as plt
from getWeather import forecast_df, response_data

#histogram of temperature
plt.hist(forecast_df['temperature'])
plt.ylabel('Temperature (C)')
plt.xlabel('Date/Time')
plt.title("Histogram of Temperature")
plt.show()