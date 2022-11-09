from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def print_hello():
    print("Hi Platzi People")

with DAG(dag_id="3-dependencias",
    description="Primer DAG with Dependencies",
    schedule_interval= "@once",
    start_date=datetime(2022, 11, 1)
) as dag:
    t1 = PythonOperator(task_id="task1",
                        python_callable=print_hello)
    
    t2 = BashOperator(task_id="Task2",
                      bash_command="echo 'Task 2'")
    
    t3 = BashOperator(task_id="task3",
                      bash_command="echo 'Task3'")
    
    t4 = BashOperator(task_id="task4",
                      bash_command="echo 'Task4'")
    
    t1>>t2 >> [t3,t4]
    t1>>t4
    t3>>t4