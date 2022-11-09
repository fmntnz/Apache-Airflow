from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG
from hellooperator import HelloOperator


with DAG(dag_id="4-customoperator",
    description="Utilizando Custom Operator",
    start_date=datetime(2022, 11, 1)    
) as dag:
    t1= HelloOperator(
        task_id="hello_Custom-Operator",
        name="Freddy M"
    )
    t1