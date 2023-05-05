import csv
import requests
import pandas as pd
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
# Define constants
lon = '18.0649'
lat = '59.3326'
app_id = os.environ['OPENWEATHER_API_KEY']

# Define API endpoint URL
url = f'https://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&appid=%s&units=metric' % (lat, lon, app_id)


# Call the API and retrieve the forecast data
def openweather_api_call(url):
    response = requests.get(url)
    data = response.json()
    # create a json file to store the raw data in data/raw folder
    with open('data/raw/raw_weather.json', 'w') as outfile:
        json.dump(data, outfile)
    # Extract relevant forecast data
    forecast_data = []
    for forecast in data['list']:
        # fetch time with timezone
        fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z")

        date_time = forecast['dt_txt']
        city = data['city']['name']
        country = data['city']['country']
        temperature = forecast['main']['temp']
        humidity = forecast['main']['humidity']
        pressure = forecast['main']['pressure']
        description = forecast['weather'][0]['description']
        min_temp = forecast['main']['temp_min']
        max_temp = forecast['main']['temp_max']
        temp = forecast['main']['temp']
        weather = forecast['weather'][0]['main']

        forecast_data.append({
            'fetch_time': fetch_time,
            'date_time': date_time,
            'city': city,
            'country': country,
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
            'description': description,
            'min_temp': min_temp,
            'max_temp': max_temp,
            'temp': temp,
            'weather': weather
            })

    # Return forecast data as dictionary
    return {'city': data['city']['name'], 'forecast': forecast_data}


print('Data retrieved from API call:. . . .')
# print(openweather_api_call(url))
print('Data stored a raw json file')

# specify the path to the folder you want to create
raw_folder_path = 'data/raw'
harmonized_folder_path = 'data/harmonized'

# use the os.makedirs() function to create the folder and any missing parent folders
os.makedirs(raw_folder_path, exist_ok = True)
os.makedirs(harmonized_folder_path, exist_ok = True)

# Get the data from the API call
data = openweather_api_call(url)

# save the data in json format
with open(raw_folder_path + '/raw_' + str(datetime.now().date()) + '.json', 'w') as f:
    json.dump(data, f)


# Transform data
def transformation(api_response):
    data_response = api_response.json()
    current_data = data_response['list']
    return current_data


response = openweather_api_call(url)

# Call the API and retrieve the forecast data
response_data = openweather_api_call(url)

# Create a Pandas DataFrame from the forecast data
forecast_df = pd.DataFrame(response_data['forecast'],
                           columns = ['fetch_time', 'date_time', 'city', 'country', 'temperature', 'humidity',
                                      'pressure', 'description', 'min_temp', 'max_temp', 'temp', 'weather'])
forecast_df['date_time'] = pd.to_datetime(forecast_df['date_time'])

print('DataFrame created:. . . .')

# Save the DataFrame as a CSV file with the current date
forecast_df.to_csv(harmonized_folder_path + f'/harmonized_data_{datetime.now().date()}.csv', index = False)
print('DataFrame saved as CSV file:. . . .')
print('Program completed successfully')

#def run_get_weather()
