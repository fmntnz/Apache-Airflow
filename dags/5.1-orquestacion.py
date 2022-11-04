from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG


with DAG(dag_id="orquestation",
    description="testing orquestation",
    schedule_interval="@weekly",
    start_date=datetime(2022, 5, 1),
    end_date=datetime(2022, 6, 1)  
) as dag:
    t1= BashOperator(
        task_id="TASK1",
        bash_command="SLEEP 2 && ECHO 'TASK1'"
    )
    t2= BashOperator(
        task_id="TASK2",
        bash_command="SLEEP 2 && ECHO 'TASK2'"
    )
    t3= BashOperator(
        task_id="TASK3",
        bash_command="SLEEP 2 && ECHO 'TASK3'"
    )
    t4= BashOperator(
        task_id="TASK4",
        bash_command="SLEEP 2 && ECHO 'TASK4'"
    )
    t1 >> t2 >> [t3,t4]