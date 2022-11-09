from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG


with DAG(dag_id="5-orquestation_1",
    description="testing orquestation",
    schedule_interval="@daily",
    start_date=datetime(2022, 5, 1),
    end_date=datetime(2022, 9, 1) ,
    default_args={"depends_on_past":True},
    max_active_runs=1
) as dag:
    t1= BashOperator(
        task_id="task1",
        bash_command="sleep 2 && echo 'task1'"
    )
    t2= BashOperator(
        task_id="task2",
        bash_command="sleep 2 && echo 'task2'"
    )
    t3= BashOperator(
        task_id="task3",
        bash_command="sleep 2 && echo 'task3'"
    )
    t4= BashOperator(
        task_id="task4",
        bash_command="sleep 2 && echo 'task4'"
    )
    t1 >> t2 >> [t3,t4]