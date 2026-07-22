"""Ejemplo deliberadamente frágil para diagnóstico; no ejecutar como solución."""

import pandas as pd

records = pandas.read_csv("Desktop/desembarques.csv")
records = records[records.quality_flag != "invalid"]
records["landings_t"] = records["landings_t"].fillna(0)
summary = records.groupby("species")["landings_t"].sum()
summary.to_csv("Desktop/final.csv")
print("listo")
