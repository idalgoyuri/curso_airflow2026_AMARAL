import pendulum # Esta biblioteca é importante para lidar com datas e horários de forma eficiente.
from random import randint
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id = "dagrundag2",
    description = "dagrundag2",
    schedule = None,  # A DAG não será executada automaticamente; será disparada manualmente.
    start_date = pendulum.datetime(2025, 1, 1, tz = "America/Sao_Paulo"),  # Data de início da DAG.
    catchup = False,  # Não executar execuções passadas que foram perdidas.
    tags = ["curso", "exemplo", "dagrundag2"],  # Tags para categorizar a DAG.
) as dag:
    
    task1 = BashOperator(task_id = "tsk1", bash_command = 'echo "{{dag_run.conf["Chave"]}}"')  # Define a tarefa tsk1 que executa o comando bash "sleep 5".

    task2 = BashOperator(task_id = "tsk2", bash_command = "sleep 5")  # Define a tarefa tsk2 que executa o comando bash "sleep 5".

    task1 >> task2  # Define a dependência entre as tarefas, garantindo que tsk2 só será executada após a conclusão de tsk1.