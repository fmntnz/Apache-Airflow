from datetime import datetime
from airflow.operators.empty import EmptyOperator
from airflow import DAG


with DAG(dag_id="5-orquestation_2",
    description="testing orquestation 2",
    schedule_interval="0 7 * * 1",
    start_date=datetime(2022, 1, 1),
    end_date=datetime(2022, 6, 1) #,
    #default_args={"depends_on_past":True},
    #max_active_runs=1"""
) as dag:
    t1= EmptyOperator(
        task_id="task1"
    )
    t2= EmptyOperator(
        task_id="task2"
    )
    t3= EmptyOperator(
        task_id="task3"
    )
    t4= EmptyOperator(
        task_id="task4"
    )
    t1 >> t2 >> t3 >> t4