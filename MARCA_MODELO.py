import pandas as pd

issues_info = pd.read_csv("issues-raw-complete.csv")
atm_info = pd.read_csv("atms-raw-complete.csv")

issues_info["MODELO"] = issues_info["MARCA_MODELO"].str.split("/").str[-1]
issues_info["MODELO"] = issues_info["MODELO"].str.split("\\").str[-1]

atm_info = atm_info[["Marca","ATM_ID"]]

issues_info = issues_info.merge(atm_info, on='ATM_ID', how='left')
del issues_info["MARCA_MODELO"]

issues_info.to_csv("FALLAS/issues-raw.csv")