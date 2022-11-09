from datetime import datetime
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator

with DAG(dag_id="7-filesensor_3",
         description="FileSensor Test",
         schedule_interval="@daily",
         start_date=datetime(2022, 5, 1),
         end_date=datetime(2022, 8, 1),
         max_active_runs=1
) as dag:
    t1 = BashOperator(
        task_id="Creating_File",
        bash_command='sleep 10 && touch /tmp/file.txt'
    )
    t2 = FileSensor(task_id="waiting_file",
                    filepath="/tmp/file.txt")
    t3 = BashOperator(
        task_id="end_task",
        bash_command='echo "The file was created successfully"'
    )
    t1 >> t2 >> t3