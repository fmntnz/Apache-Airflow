from airflow.models.baseoperator import BaseOperator

class NotifyOperator(BaseOperator):
    
        def __init__(self,date:str,**kwargs):
            super().__init__(**kwargs)
            self.date=date
        def execute(self,context):
            print(f"Hi Data team, Space X data for {self.date}  are now available!.. Please check them out!")