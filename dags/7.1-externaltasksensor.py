from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="7-externalTaskSensor_1",
    description="testing external Task Sensor 1",
    schedule_interval="@daily",
    start_date=datetime(2022, 5, 1),
    end_date=datetime(2022, 8, 1)
) as dag:
    t1= BashOperator(
        task_id="task1",
        bash_command="sleep 10 && echo 'Dag for task1 finished'", 
        depends_on_past=True
    
    )
    t1