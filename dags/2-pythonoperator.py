from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_hello():
    print("Hi Platzi People")

with DAG(dag_id="pythonoperator",
    description="Primer DAG with Pythgon Operator",
    schedule_interval= "@once",
    start_date=datetime(2022, 11, 1)
) as dag:
    t1 = PythonOperator(task_id="hello_with_python",
                        python_callable=print_hello)
    t1