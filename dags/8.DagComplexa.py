import pendulum # Esta biblioteca é importante para lidar com datas e horários de forma eficiente.
from airflow import DAG

# Adicione a nova importação atualizada:
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id = "dag_complexa",
    description = "DAG complexa com múltiplas tarefas e dependências",
    schedule = None,  # A DAG não será executada automaticamente; será disparada manualmente.
    start_date = pendulum.datetime(2025, 1, 1, tz = "America/Sao_Paulo"),  # Data de início da DAG.
    catchup = False,  # Não executar execuções passadas que foram perdidas.
    tags = ["curso", "exemplo", "complexa"],  # Tags para categorizar a DAG.
) as dag:
    task1 = BashOperator(task_id = "tsk1", bash_command = "sleep 5")
    task2 = BashOperator(task_id = "tsk2", bash_command = "sleep 5")
    task3 = BashOperator(task_id = "tsk3", bash_command = "sleep 5")
    task4 = BashOperator(task_id = "tsk4", bash_command = "sleep 5")
    task5 = BashOperator(task_id = "tsk5", bash_command = "sleep 5")
    task6 = BashOperator(task_id = "tsk6", bash_command = "sleep 5")
    task7 = BashOperator(task_id = "tsk7", bash_command = "sleep 5")
    task8 = BashOperator(task_id = "tsk8", bash_command = "sleep 5")
    task9 = BashOperator(task_id = "tsk9", bash_command = "sleep 5")

    task1 >> task2
    task3 >> task4
    [task2, task4] >> task5 >> task6
    task6 >> [task7, task8, task9]  # Define que as tasks 7, 8 e 9 serão executadas em paralelo após a execução da task 6.
