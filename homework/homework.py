"""
Escriba el codigo que ejecute la accion solicitada.
"""

# pylint: disable=import-outside-toplevel


from homework.extracted_data import lectura_archivos_zip
from homework.extracted_data import validacion_datos
from homework.extracted_data import concatenar_archivos

from homework.transformation import client
from homework.transformation import campaign
from homework.transformation import economics

def extracted_data():
    lista_archivos = lectura_archivos_zip()
    validacion_datos(lista_archivos)
    bank_marketing_campaing_df = concatenar_archivos(lista_archivos)

    return bank_marketing_campaing_df

bank_marketing_campaing_df =extracted_data()

client(bank_marketing_campaing_df)
campaign(bank_marketing_campaing_df)
economics(bank_marketing_campaing_df)

def clean_campaign_data():
    """
    En esta tarea se le pide que limpie los datos de una campaña de
    marketing realizada por un banco, la cual tiene como fin la
    recolección de datos de clientes para ofrecerls un préstamo.

    La información recolectada se encuentra en la carpeta
    files/input/ en varios archivos csv.zip comprimidos para ahorrar
    espacio en disco.

    Usted debe procesar directamente los archivos comprimidos (sin
    descomprimirlos). Se desea partir la data en tres archivos csv
    (sin comprimir): client.csv, campaign.csv y economics.csv.
    Cada archivo debe tener las columnas indicadas.

    Los tres archivos generados se almacenarán en la carpeta files/output/.

    client.csv:
    - client_id
    - age
    - job: se debe cambiar el "." por "" y el "-" por "_"
    - marital
    - education: se debe cambiar "." por "_" y "unknown" por pd.NA
    - credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    - mortage: convertir a "yes" a 1 y cualquier otro valor a 0

    campaign.csv:
    - client_id
    - number_contacts
    - contact_duration
    - previous_campaing_contacts
    - previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    - campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    - last_contact_day: crear un valor con el formato "YYYY-MM-DD",
        combinando los campos "day" y "month" con el año 2022.

    economics.csv:
    - client_id
    - const_price_idx
    - eurobor_three_months



    """

    client(bank_marketing_campaing_df)
    campaign(bank_marketing_campaing_df)
    economics(bank_marketing_campaing_df)

    return print("Los archivos han sido limpiados y almacenados en la carpeta files/output/")


if __name__ == "__main__":
    clean_campaign_data()
