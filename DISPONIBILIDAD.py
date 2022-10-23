import pandas as pd
import random 

DF_DISPONIBILIDAD = pd.DataFrame(columns=["ATM_ID","HOURS","DIAS_SEMANA"])

atm_info = pd.read_csv("atms-raw.csv")

LISTA_HOURS = ["00","03","06","09","12","15","18","21"]

LISTA_SEMANA_DIAS = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

for x in atm_info["ATM"]:
    print (x)
    for y in LISTA_HOURS:
        for z in LISTA_SEMANA_DIAS:
            DF_DISPONIBILIDAD.loc[len(DF_DISPONIBILIDAD.index)] = [x,y,z] 

DF_DISPONIBILIDAD.to_csv("DF_DISPONIBILIDAD.csv", index=False)