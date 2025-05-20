import pandas as pd
import requests

url ="http://service.stmk.gv.at/ogd/OGD_Data_ABT17/statistik/PENDLER/STMK_31102016_PENDLER.csv"

resp = requests.get(url)
with open("STMK_31102016_PENDLER.csv", "wb") as f:
    f.write(resp.content)

df = pd.read_csv("STMK_31102016_PENDLER.csv", sep=";", encoding="latin1")

print(df.head())

bezirke = df["DISTRICT_NAME"].unique()
print("Bezirke:", bezirke)

print(df["COMUTERS_IN"].sum())

print(df[df["LAU_NAME"].apply(len).idxmax()]["LAU_NAME"])
