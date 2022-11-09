from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(dag_id="0-primerdag",
            description="Nuestro primer DAG",
            start_date=datetime(2022, 12, 1),
            schedule_interval="@once") as dag:
    t1=EmptyOperator(task_id="dummy")
    t1
