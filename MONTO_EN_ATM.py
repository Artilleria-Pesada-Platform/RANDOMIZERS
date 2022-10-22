import pandas as pd
import random 

DF_MONTO = pd.DataFrame(columns=["ATM_ID","MONTO_ACTUAL"])

def Randomizer_MONTO(DF_MONTO):
    atm_info = pd.read_csv("atms-raw.csv")
    monto_actual = [x for x in range(50000,500000,1000)]

    for x in list(atm_info["ATM"]):
        temp_monto_actual = random.choice(monto_actual)

        DF_MONTO.loc[len(DF_MONTO.index)] = [x,temp_monto_actual] 

Randomizer_MONTO(DF_MONTO)
DF_MONTO.to_csv("MONTO_ACTUAL/DF_MONTO.csv")
        