from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


# default_args = {
#     'owner': 'sobhi',
#     'retries': 5,
#     'retry_delay': timedelta(minutes = 5)
#     }



#with DAG(
    #    default_args = default_args,
     #   dag_id = 'Weather_Forcast_Postgres_01',
     #   description = 'Our first dag using python operator',
     #   start_date = datetime(2021, 10, 6),
     #   schedule_interval = '@daily'
     #   ) as dag:


