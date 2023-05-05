
import matplotlib.pyplot as plt

from getWeather import forecast_df, response_data

# Plot the temperature data using Matplotlib
plt.plot(forecast_df['date_time'], forecast_df['temperature'])
plt.xlabel('Date/Time')
plt.ylabel('Temperature (C)')
plt.title(f"Temperature forecast for {response_data['city']}")
plt.show()
