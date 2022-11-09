from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG

def myfunction():
        pass

with DAG(dag_id="6-monitoring_1",
    description="Monitoring our DAG",
    schedule_interval="@daily",
    start_date=datetime(2022, 1, 1),
    end_date=datetime(2022, 1, 10)
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
    t4= python_task = PythonOperator(
        task_id="task4",
        python_callable=myfunction
    )
    t5= BashOperator(
        task_id="task5",
        bash_command="sleep 2 && echo 'task5'"
    )
    t1 >> t2 >> t3 >> t4 >> t5