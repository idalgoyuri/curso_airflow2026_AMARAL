import pendulum # Esta biblioteca é importante para lidar com datas e horários de forma eficiente.
from airflow import DAG
# Adicione a nova importação atualizada:
from airflow.providers.standard.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule

with DAG(
    dag_id = "triggerdag3",  # Identificador único da DAG.
    description = "Trigger DAG 3",  # Descrição da DAG.
    schedule = None,  # A DAG não será executada automaticamente; será disparada manualmente.
    start_date = pendulum.datetime(2025, 1, 1, tz = "America/Sao_Paulo"),  # Data de início da DAG.
    catchup = False,  # Não executar execuções passadas que foram perdidas.
    tags = ["curso", "exemplo"],  # Tags para categorizar a DAG.
) as dag:
    task1 = BashOperator(task_id = "tsk1", bash_command = "exit 1")
    task2 = BashOperator(task_id = "tsk2", bash_command = "exit 1")
    task3 = BashOperator(task_id = "tsk3", bash_command = "sleep 5", trigger_rule = TriggerRule.ALL_FAILED)  

    [task1 ,task2] >> task3 