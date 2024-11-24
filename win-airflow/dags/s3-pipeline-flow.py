
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import boto3 
from airflow.models import Variable

s3=boto3.resource(
        service_name='s3',
        region_name='ap-south-1',
        aws_access_key_id=Variable.get("aws-access-key-id"),
        aws_secret_access_key=Variable.get("aws-access-key")
    )

def list_bucket_name():
        for bucket in s3.buckets.all():
            print(bucket.name)



with DAG(
    "s3-pipeline-flow",
    default_args={
        "depends_on_past":False,
        "email":["airflow@gmail.com"],
        "email_on_failure":False,
        "email_on_retry":False,
        "retries":1,
        "retry_delay":timedelta(minutes=5),
    },
    description="simple dag to copy the a file from server to S3",
    schedule=timedelta(days=1),
    start_date=datetime(2024,11,23),
    catchup=False,
    tags=["S3-load-test"]
) as dag:

    task1=PythonOperator(
        task_id='list_bucket_name',
        python_callable=list_bucket_name

    )


    task1
    
