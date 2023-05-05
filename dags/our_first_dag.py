from datetime import timedelta, datetime
from airflow.operators.bash import BashOperator

from airflow import DAG
from airflow.operators.python import PythonOperator

def get_sklearn():
    import sklearn
    print(f"sklearn with version: {sklearn.__version__} ")

default_args = {
    'owner': 'sobhi',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily'
) as dag:
    #PythonOperator
    task1 = PythonOperator(
        task_id = 'get_sklearn',
        python_callable = get_sklearn
        )
    task1
