from airflow.models.dag import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.models import Variable

def t1():
    a=5+2
    print(a)

def t2():
    b=4+2
    print(b)

with DAG (
        "test-2",
        default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["test2"],
) as dag:

    task1=PythonOperator(
        task_id='task--1',
        python_callable=t1
    )

    task2=PythonOperator(
        task_id='task--2',
        python_callable=t2
    )

    task1 >> task2


