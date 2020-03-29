from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator


dag = DAG('hellow_world', description='spark-job',
          schedule_interval='0 12 * * *',
          start_date=datetime(2020, 3, 29), catchup=False)

spark_submit_task = SparkSubmitOperator(
    task_id='spark-submit',
    conn_id='spark-local',
    py_files='/usr/local/airflow/spark/jobs/hello_world/packages/packages.zip',
    application='/usr/local/airflow/spark/jobs/hello_world/000_hello_world.py',
    dag=dag
)

spark_submit_task

