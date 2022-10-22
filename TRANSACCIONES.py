import pandas as pd
import datetime as dt
import random 

#7957 --DISPENSADOR
#15   --AUTOBANCO
#5810 --PRACTICAJA

DF_TRANSACCIONES_SEPTIEMBRE = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_OCTUBRE = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_NOVIEMBRE = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_DICIEMBRE = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_ENERO = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_FEBRERO = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_MARZO = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_ABRIL = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_MAYO = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_JUNIO = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_JULIO = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])
DF_TRANSACCIONES_AGOSTO = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])

def Randomizer_TRANSACCIONES(num_registros_by_cajero_min,num_registros_by_cajero_max,month, year, DF_TRANSACCIONES):
    print("hELLO")
    tipo_transaccion = ["DEPOSITO","RETIRO"]
    monto_retiro = [x for x in range(100,9400,100)]
    monto_retiro_d = [x for x in range(100,50000,100)]
    
    atm_info = pd.read_csv("atms-raw.csv")

    if month in (1,3,5,7,8,10,12):
        month_day = [y for y in range(1,32,1)]
    elif month in(4,6,9,11):
        month_day = [y for y in range(1,31,1)]
    else:
        month_day = [y for y in range(1,28,1)]

    for x in list(atm_info[atm_info["Tipo dispositivo"] != 'PRACTDUAL']["ATM"]):
        tipo_d = "DISPENSADOR"
        num_registros_by_cajero = random.randrange(num_registros_by_cajero_min,num_registros_by_cajero_max,1)
        for y in range(num_registros_by_cajero):
            temp_date = str(random.choice(month_day))+"/"+str(month)+"/"+str(year)
            temp_transaccion = tipo_transaccion[1]
            temp_monto_retiro = random.choice(monto_retiro)

            DF_TRANSACCIONES.loc[len(DF_TRANSACCIONES.index)] = [x,tipo_d,temp_transaccion,temp_monto_retiro,temp_date] 
            
    for x in list(atm_info[atm_info["Tipo dispositivo"] == 'PRACTDUAL']["ATM"]):
        tipo_d = "PRACTDUAL"
        num_registros_by_cajero = random.randrange(num_registros_by_cajero_min,num_registros_by_cajero_max,1)
        for y in range(num_registros_by_cajero):
            temp_date = str(random.choice(month_day))+"/"+str(month)+"/"+str(year)
            temp_transaccion = random.choice(tipo_transaccion)

            if (temp_transaccion == "DEPOSITO" ):
                temp_monto_retiro = random.choice(monto_retiro_d)
            else:
                temp_monto_retiro = random.choice(monto_retiro)

            DF_TRANSACCIONES.loc[len(DF_TRANSACCIONES.index)] = [x,tipo_d,temp_transaccion,temp_monto_retiro,temp_date] 

#Randomizar 09/2021 al 08/2022    

Randomizer_TRANSACCIONES(3,15,9, 2021,DF_TRANSACCIONES_SEPTIEMBRE)
DF_TRANSACCIONES_SEPTIEMBRE.to_csv("TRANSACCIONES/DF_TRANSACCIONES_SEPTIEMBRE.csv")
Randomizer_TRANSACCIONES(3,15,10, 2021,DF_TRANSACCIONES_OCTUBRE)
DF_TRANSACCIONES_OCTUBRE.to_csv("TRANSACCIONES/DF_TRANSACCIONES_OCTUBRE.csv")
Randomizer_TRANSACCIONES(3,15,11, 2021,DF_TRANSACCIONES_NOVIEMBRE)
DF_TRANSACCIONES_NOVIEMBRE.to_csv("TRANSACCIONES/DF_TRANSACCIONES_NOVIEMBRE.csv")
Randomizer_TRANSACCIONES(3,15,12, 2021,DF_TRANSACCIONES_DICIEMBRE)
DF_TRANSACCIONES_DICIEMBRE.to_csv("TRANSACCIONES/DF_TRANSACCIONES_DICIEMBRE.csv")
Randomizer_TRANSACCIONES(3,15,1, 2022,DF_TRANSACCIONES_ENERO)
DF_TRANSACCIONES_ENERO.to_csv("TRANSACCIONES/DF_TRANSACCIONES_ENERO.csv")
Randomizer_TRANSACCIONES(3,15,2, 2022,DF_TRANSACCIONES_FEBRERO)
DF_TRANSACCIONES_FEBRERO.to_csv("TRANSACCIONES/DF_TRANSACCIONES_FEBRERO.csv")
Randomizer_TRANSACCIONES(3,15,3, 2022,DF_TRANSACCIONES_MARZO)
DF_TRANSACCIONES_MARZO.to_csv("TRANSACCIONES/DF_TRANSACCIONES_MARZO.csv")
Randomizer_TRANSACCIONES(3,15,4, 2022,DF_TRANSACCIONES_ABRIL)
DF_TRANSACCIONES_ABRIL.to_csv("TRANSACCIONES/DF_TRANSACCIONES_ABRIL.csv")
Randomizer_TRANSACCIONES(3,15,5, 2022,DF_TRANSACCIONES_MAYO)
DF_TRANSACCIONES_MAYO.to_csv("TRANSACCIONES/DF_TRANSACCIONES_MAYO.csv")
Randomizer_TRANSACCIONES(3,15,6, 2022,DF_TRANSACCIONES_JUNIO)
DF_TRANSACCIONES_JUNIO.to_csv("TRANSACCIONES/DF_TRANSACCIONES_JUNIO.csv")
Randomizer_TRANSACCIONES(3,15,7, 2022,DF_TRANSACCIONES_JULIO)
DF_TRANSACCIONES_JULIO.to_csv("TRANSACCIONES/DF_TRANSACCIONES_JULIO.csv")
Randomizer_TRANSACCIONES(3,15,8, 2022,DF_TRANSACCIONES_AGOSTO)
DF_TRANSACCIONES_AGOSTO.to_csv("TRANSACCIONES/DF_TRANSACCIONES_AGOSTO.csv")

#Randomizer_TRANSACCIONES(5,15,1,3,3, 2021,DF_TRANSACCIONES)

#117,827  --12 min

