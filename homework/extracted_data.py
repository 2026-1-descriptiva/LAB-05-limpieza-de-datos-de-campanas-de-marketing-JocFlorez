import pandas as pd
from zipfile import ZipFile
from pathlib import Path
import os

def lectura_archivos_zip():
    lista_archivos = []
    archivos = Path("files/input").glob("*.csv.zip")

    for archivo in archivos:
        temporal_df = pd.read_csv(archivo, index_col=0, compression="zip")
        lista_archivos.append(temporal_df)

    return lista_archivos

def validacion_datos(lista_archivos):
    estructura = ["client_id", "age", "job", "marital", "education", 
    "credit_default", "mortgage", "month", "day", 
    "contact_duration", "number_contacts", "previous_campaign_contacts", 
    "previous_outcome", "cons_price_idx", "euribor_three_months", "campaign_outcome"]

    for df in lista_archivos:
        if not all(col in df.columns for col in estructura):
            raise ValueError("El archivo no tiene la estructura esperada")
    
    return print("Todos los archivos tienen la estructura esperada")



def concatenar_archivos(lista_archivos):
    bank_marketing_campaing_df = pd.concat(lista_archivos, ignore_index=True)
    return bank_marketing_campaing_df

