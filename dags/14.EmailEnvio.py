import pendulum # Esta biblioteca é importante para lidar com datas e horários de forma eficiente.
from airflow import DAG
from airflow.providers.smtp.operators.smtp import EmailOperator

with DAG(
    dag_id = "teste_email_dag",
    description = "Envio de Email",
    schedule = None,  # A DAG não será executada automaticamente; será disparada manualmente.
    start_date = pendulum.datetime(2025, 1, 1, tz = "America/Sao_Paulo"),  # Data de início da DAG.
    catchup = False,  # Não executar execuções passadas que foram perdidas.
    tags = ["curso", "exemplo"],  # Tags para categorizar a DAG.
) as dag:
    EmailOperator(
        task_id = "send_email",
        to = ['yuriidalgo@gmail.com', 'yuriidalgosilva@prefeitura.sp.gov.br'],
        subject = "Teste de envio de e-mail no Airflow",
        html_content = "<h3>Este é um teste de envio de e-mail usando o Airflow!</h3>",


    )