import json
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from FinalPersonalProject_Notification import NotifyOperator

default_args={'schedule_interval':"0 7 * * 1",
         'start_date':datetime(2022, 10, 1),
         'end_date':datetime.now(), 
         'depend_on_past':True}

def _generate_platzi_data(**kwargs):
    import pandas as pd
    data = pd.DataFrame({"student":["Maria Cruz", "Daniel Crema", "Elon Musk", "Karol Castrejon", "Freddy Vega", "Freddy Montañez"], 
                         "timestamp":[kwargs['logical_date'], kwargs['logical_date'],kwargs['logical_date'],kwargs['logical_date'],kwargs['logical_date'],kwargs['logical_date']]
                         })
    data.to_csv(f"/tmp/platzi_data_{kwargs['ds_nodash']}.csv",header=True)

with DAG(dag_id='MyPersonalAirflowProject',
         description="This DAG is the final project of the 'APACHE AIRFLOW FOUNDATIONS' course in PLATZI",
         default_args=default_args,
         max_active_runs=1
)as dag:
    nasa_verification_task=BashOperator(task_id="nasa_verification_task",
                                        bash_command='sleep 20 && echo "OK"> /tmp/reponse_{{ds_nodash}}.txt')
    
    t2 = FileSensor(task_id="waiting_nasa_confirmation",
                    filepath="/tmp/reponse_{{ds_nodash}}.txt",
                    poke_interval=20)
    t3 = BashOperator(
        task_id="end_confirmation_from_nasa",
        bash_command='echo "The Confirmation file was created successfully"'
    )
    spaceX_data=BashOperator(task_id="SpaceX_data",
                             bash_command="curl -o /tmp/history.json -L 'https://api.spacexdata.com/v4/history'")
    
    copy_data_to_local = PythonOperator(
        task_id="copy_data_to_local",
        python_callable=_generate_platzi_data
    )
    visualize_data = BashOperator(task_id="Print_Imported_data",
                                  bash_command='ls /tmp/ && head /tmp/platzi_data_{{ds_nodash}}.csv')
    Notify_Data = NotifyOperator(
                                    task_id="Data_Team_Notification",
                                    date=str(datetime.now().date())
    )
    Notify_Marketing = BashOperator(
                                    task_id="Marketing_team_Notification",
                                    bash_command='echo "Hi Marketing team, Space X data for {{ds}} are now available!.. Please check them out!"'
    )
    nasa_verification_task>>t2>>t3>>spaceX_data>>copy_data_to_local>>visualize_data >> [Notify_Data, Notify_Marketing]

