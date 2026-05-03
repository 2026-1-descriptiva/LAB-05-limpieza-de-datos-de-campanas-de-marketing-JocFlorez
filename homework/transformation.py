import pandas as pd
from zipfile import ZipFile
from pathlib import Path
import os

def client (df):
    client_df = df[["client_id", "age", "job", "marital","education","credit_default","mortgage"]].copy()
    client_df["job"] = client_df["job"].str.replace(".","",regex=False).str.replace("-","_", regex=True)
    client_df["education"] = client_df["education"].str.replace(".","_",regex=False).replace("unknown",pd.NA)
    client_df["credit_default"] = client_df["credit_default"].apply(lambda x: 1 if x == "yes" else 0)
    client_df["mortgage"] = client_df["mortgage"].apply(lambda x : 1 if x == "yes" else 0)

    output_path = Path("files/output/client.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    return client_df.to_csv(output_path, index=False)

def campaign (df):
    campaign_df = df[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome", "day", "month"]].copy()
    campaign_df["previous_outcome"] = df["previous_outcome"].apply(lambda x : 1 if x == "success" else 0)
    campaign_df["campaign_outcome"] = df["campaign_outcome"].apply(lambda x : 1 if x == "yes" else 0)
    campaign_df["last_contact_date"] = pd.to_datetime(campaign_df["day"].astype(str) + "-" + campaign_df["month"] + "-2022", format="%d-%b-%Y")
    campaign_df.drop(columns=["day", "month"], inplace=True)

    output_path = Path("files/output/campaign.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    return campaign_df.to_csv(output_path, index=False)

def economics (df):
    economics_df = df[["client_id", "cons_price_idx", "euribor_three_months"]].copy()
    output_path = Path("files/output/economics.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    return economics_df.to_csv(output_path, index=False)