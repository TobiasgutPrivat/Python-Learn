import pandas as pd
from io import StringIO

data = """FRUITS;MARCH;APRIL
Apples;10;14
Bananas;10;12
Oranges;12;15
Cherries;32;42
"""

try:
    df = pd.read_csv("http://opendata.ch/musterlösung.csv", sep=";", encoding="utf-8")
except:
    df = pd.read_csv(StringIO(data), sep=";", encoding="utf-8")

# 2) Erweitern Sie den DataFrame um eine Spalte "TOTAL", welcher die Summe aus den
# Spalten für März und April enthält.

df["TOTAL"] = df["MARCH"] + df["APRIL"]

print(df)