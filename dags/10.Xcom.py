import pendulum # Esta biblioteca é importante para lidar com datas e horários de forma eficiente.
from airflow import DAG
from airflow.sdk import task
from random import randint

with DAG(
    dag_id = "Xcom_1",
    description = "Xcom",
    schedule = None,  # A DAG não será executada automaticamente; será disparada manualmente.
    start_date = pendulum.datetime(2025, 1, 1, tz = "America/Sao_Paulo"),  # Data de início da DAG.
    catchup = False,  # Não executar execuções passadas que foram perdidas.
    tags = ["curso", "exemplo", "Xcom"],  # Tags para categorizar a DAG.
) as dag:
    @task
    def task_write():
        value = randint(1, 1000)
        return {"value_teste":value}  # Retorna um dicionário com a chave "value_teste" e o valor gerado aleatoriamente.
    
    @task
    def task_read(pay_load: dict):
        print(f"Valor recebido: {pay_load['value_teste']}")  # Imprime o valor recebido no console.

    task_read(task_write())  # Chama a task_read passando o retorno da task_write como argumento.