from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.sensors.external_task import ExternalTaskSensor

with DAG(dag_id="7-externalTaskSensor_2",
    description="testing secondary DAG for external Task Sensor",
    schedule_interval="@daily",
    start_date=datetime(2022, 5, 1),
    end_date=datetime(2022, 8, 1),
    max_active_runs=1
) as dag:
    t1= ExternalTaskSensor(
        task_id="waiting_DAG",
        external_dag_id="7-externalTaskSensor_1",
        external_task_id="task1",
        poke_interval=10
    )
    t2= BashOperator(
        task_id="task2",
        bash_command="sleep 10 && echo 'Dag 2 finished'", 
        depends_on_past=True
    ) 
    t1 >> t2