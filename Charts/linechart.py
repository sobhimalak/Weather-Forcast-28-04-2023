import csv
import json
import pandas as pd
import matplotlib.pyplot as plt
import getWeather
from getWeather import forecast_df, response_data, openweather_api_call

# print max temperature for each day
weather_data = openweather_api_call(getWeather.url)

# Create a list of dictionaries to store the cleaned up weather data
clean_data = []
for day, value in enumerate(weather_data['forecast']):
    max_temp = value['max_temp']
    min_temp = value['min_temp']
    # clean data have day as number,
    clean_data.append({'Day': day + 1, 'max_temp': max_temp, 'min_temp': min_temp})

# Save the list of dictionaries to a JSON file
with open(getWeather.harmonized_folder_path + f'clean_data.json', 'w') as outfile:
    json.dump(clean_data, outfile)

# Save the list of dictionaries to a CSV file
with open(getWeather.harmonized_folder_path + f'clean_data.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(clean_data[0].keys())
    for row in clean_data:
        writer.writerow(row.values())

# Scatter plot with day on the x-axis and max temperature and min temperature on the y-axis for each day color bar
day_list = [day['Day'] for day in clean_data]

# indicates the temperature
plt.scatter(day_list, forecast_df['max_temp'], c=forecast_df['max_temp'], cmap='coolwarm')
plt.scatter(day_list, forecast_df['min_temp'], c=forecast_df['min_temp'], cmap='coolwarm')
plt.title('Max and Min Temperature forcast')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.colorbar()
plt.show()

