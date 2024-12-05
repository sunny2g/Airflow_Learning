import os
from airflow import DAG
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator

# Import the environment configuration
import Dev.config.env_config

# Now you can access the environment variables set in env_config.py
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 3,
}

def print_var():
    print(DATABASE_URL)

with DAG(
    'my_dev_dummy_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=["DEV"],
) as dag:

    start_task = DummyOperator(task_id='start')

    # You can use the environment variables wherever needed
    print(f"Connecting to database at {DATABASE_URL}")
    print(f"Using API key: {API_KEY}")
    print(f"Accessing S3 bucket: {S3_BUCKET_NAME}")

    print_variables = PythonOperator(
        task_id='print_var',
        python_callable=print_var
    )    



    start_task >> print_variables
