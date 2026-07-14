import pendulum # Esta biblioteca é importante para lidar com datas e horários de forma eficiente.
from random import randint
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import get_current_context

with DAG(
    dag_id = "Xcom_2",
    description = "Xcom_2",
    schedule = None,  # A DAG não será executada automaticamente; será disparada manualmente.
    start_date = pendulum.datetime(2025, 1, 1, tz = "America/Sao_Paulo"),  # Data de início da DAG.
    catchup = False,  # Não executar execuções passadas que foram perdidas.
    tags = ["curso", "exemplo", "Xcom2"],  # Tags para categorizar a DAG.
) as dag:
    # Criando as funções que serão chamadas pelas tasks
    def task_write():
        ti = get_current_context()["ti"]  # Obtém o contexto atual da execução da DAG.
        ti.xcom_push(key = "value_teste", value = randint(1, 1000))  # Gera um valor aleatório e o envia para o XCom com a chave "value_teste".
    
    def task_read():
        ti = get_current_context()["ti"]  # Obtém o contexto atual da execução da DAG.
        value = ti.xcom_pull(key = "value_teste", task_ids = "tsk1")  # Recupera o valor do XCom usando a chave "value_teste" e o ID da tarefa "tsk1".
        print(f"Valor recebido: {value}")  # Imprime o valor recebido no console.
    
    # Observe que estamos usando funções python acima, e as mesmas devem ser chamadas nas tasks

    task1 = PythonOperator(task_id = "tsk1", python_callable = task_write)  # Define a tarefa tsk1 que executa a função task_write.
    task2 = PythonOperator(task_id = "tsk2", python_callable = task_read)  # Define a tarefa tsk2 que executa a função task_read.

    task1 >> task2  # Define a dependência entre as tarefas, garantindo que tsk2 só será executada após a conclusão de tsk1.