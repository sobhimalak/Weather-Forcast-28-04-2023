import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from getWeather import harmonized_folder_path

# load environment variables
load_dotenv()


def make_database():

    try:
        conn = psycopg2.connect(
            database = os.getenv('POSTGRES_DB'),
            user = os.getenv('POSTGRES_USER'),
            password = os.getenv('POSTGRES_PASSWORD'),
            host = os.getenv('POSTGRES_HOST'),
            port = os.getenv('POSTGRES_PORT')
            )
        cursor = conn.cursor()
        print("Connected to Database Successfully. . .")

        # sql statement to create table
        create_table = """CREATE TABLE IF NOT EXISTS weather_app
                (
                    fetch_time   TIMESTAMP,
                    date_time    TIMESTAMP,
                    city         TEXT,
                    country      TEXT,
                    temperature  REAL,
                    humidity     REAL,
                    description  TEXT,
                    pressure     REAL,
                    min_temp     REAL,
                    max_temp     REAL,
                    temp         REAL,
                    weather      TEXT
                );
                """

        # executing sql statement
        cursor.execute(create_table)

        # specify the path to the folder containing the CSV files
        folder_path = harmonized_folder_path
        # use the os.listdir() function to list all CSV files in the folder
        csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
        # loop through the files and read them in with pandas
        # select the latest CSV file
        if len(csv_files) > 0:
            csv_path = os.path.join(folder_path, csv_files[1])
            forecast = pd.read_csv(csv_path)
            print(csv_path)

        # insert data into table
            cursor.executemany("""
            INSERT INTO weather_app (
                fetch_time,
                date_time,
                city,
                country,
                temperature,
                humidity,
                description,
                pressure,
                min_temp,
                max_temp,
                temp,
                weather
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)
                    """,
                               [
                                   (
                                       row["fetch_time"],
                                       row["date_time"],
                                       row["city"],
                                       row["country"],
                                       row["temperature"],
                                       row["humidity"],
                                       row["description"],
                                       row["pressure"],
                                       row["min_temp"],
                                       row["max_temp"],
                                       row["temp"],
                                       row["weather"],
                                       )
                                   for index, row in forecast.iterrows()
                                   ],
                               )

        conn.commit()
        print("Table Created Successfully . . .")

        conn.close()
        cursor.close()
        print("Connection Closed . . . ")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to database : ", error, "\n", "Please check your file Name. and try again . . .")


# executing python code
if __name__ == "__main__":
    make_database()
