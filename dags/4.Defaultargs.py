import pendulum # Esta biblioteca é importante para lidar com datas e horários de forma eficiente.
from datetime import timedelta
from airflow import DAG

# Adicione a nova importação atualizada:
from airflow.providers.standard.operators.bash import BashOperator

# Estrutura de dicionário padrão da linguagem Python, que contém os argumentos padrão para a DAG.
default_args = {
    "depends_on_past": False,  # A execução da DAG não depende da execução anterior.
    "email" : ["teste@email.com"],
    "email_on_failure": False,  # Não enviar e-mail em caso de falha.
    "email_on_retry": False,  # Não enviar e-mail em caso de tentativa de reexecução.
    "retries": 1, # Número de tentativas de reexecução em caso de falha.
    "retry_delay": timedelta(seconds = 10),  # Intervalo de tempo entre as tentativas de reexecução.
}
# Observe que os argumento padrão definidos no dicionário default_args serão aplicados a todas as tasks.
with DAG(
    dag_id = "defaultargs_dag",
    description = "Minha quarta DAG com default_args(teste).",
    schedule = None,  # A DAG não será executada automaticamente; será disparada manualmente.
    start_date = pendulum.datetime(2025, 1, 1, tz = "America/Sao_Paulo"),  # Data de início da DAG.
    catchup = False,  # Não executar execuções passadas que foram perdidas.
    tags = ["args", "exemplo prático"],  # Tags para categorizar a DAG.
) as dag:
    task1 = BashOperator(task_id = "tsk1", bash_command = "sleep 5", retries = 3)  # Sobrescrevendo os argumentos padrão da DAG para esta task específica.
    task2 = BashOperator(task_id = "tsk2", bash_command = "sleep 5")
    task3 = BashOperator(task_id = "tsk3", bash_command = "sleep 5")

    task1 >> task2 >> task3  

