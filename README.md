Sure, here is an example of how you could incorporate both code snippets into the README:

## Weather App

This is a simple Python weather app that retrieves weather data for a given city and stores it in a PostgreSQL database.

### Prerequisites

To run this app, you will need:

- Python 3
- The `dotenv`, `pandas`, `psycopg2`, and `requests` Python libraries
- A PostgreSQL database

### Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries by running `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory of the project with the following contents:
```
API_KEY=<your OpenWeatherMap API key>
POSTGRES_DB=<your PostgreSQL database name>
POSTGRES_USER=<your PostgreSQL username>
POSTGRES_PASSWORD=<your PostgreSQL password>
POSTGRES_HOST=<your PostgreSQL host>
POSTGRES_PORT=<your PostgreSQL port>
```
4. Replace the values with your own API key and database credentials.

### Usage

To run the app, simply execute the following command:

```
python app.py
```

This will prompt you to enter a city name. Once you enter a valid city name, the app will retrieve the weather data for that city and store it in the PostgreSQL database.

To view the data in the database, you can run the following command:

```
python database.py
```

This will create a `weather_app` table in the database (if it doesn't already exist) and insert the weather data. You can then view the data by querying the table using a PostgreSQL client.

### Example

Here is an example of what the output of the `app.py` script might look like:

```
Enter city name: San Francisco
Retrieving weather data for San Francisco. . .
City: San Francisco
Country: US
Temperature: 13.48°C
Humidity: 81%
Description: scattered clouds
Pressure: 1015 hPa
Minimum Temperature: 11.67°C
Maximum Temperature: 16.11°C
Temperature: 13.48°C
Weather: {'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}

Weather data saved to database.
```

And here is an example of what the `database.py` script might look like:

```
Connected to Database Successfully. . .
Table Created Successfully . . .
Connection Closed . . .
```