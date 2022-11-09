from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
from airflow.utils.trigger_rule import TriggerRule

def myfunction():
    raise Exception

default_args={}


with DAG(dag_id="6-monitoring_2",
    description="testing monitoring 2",
    schedule_interval="@daily",
    start_date=datetime(2022, 1, 1),
    end_date=datetime(2022, 1, 5) ,
    default_args=default_args,
    max_active_runs=1
) as dag:
    t1= BashOperator(
        task_id="task1",
        bash_command="sleep 5 && echo 'task1'", 
        trigger_rule=TriggerRule.ALL_SUCCESS,
        retries=2,
        retry_delay=5,
        depends_on_past=False
    )
    t2= BashOperator(
        task_id="task2",
        bash_command="sleep 3 && echo 'task2'",
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=True
    )
    t3= BashOperator(
        task_id="task3",
        bash_command="sleep 2 && echo 'task3'",
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALWAYS,
        depends_on_past=True
    )
    t4= python_task = PythonOperator(
        task_id="task4",
        python_callable=myfunction,
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=True
    )
    t5= BashOperator(
        task_id="task5",
        bash_command="sleep 2 && echo 'task5'",
        retries=2,
        retry_delay=5,
        depends_on_past=True
    )
    t1 >> t2 >> t3 >> t4 >> t5