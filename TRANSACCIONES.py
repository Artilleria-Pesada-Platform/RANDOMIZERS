import pandas as pd
import datetime as dt
import random 

#7957 --DISPENSADOR
#15   --AUTOBANCO
#5810 --PRACTICAJA

DF_TRANSACCIONES = pd.DataFrame(columns=["ATM_ID","ATM_TYPE","TRANSACTION_TYPE","AMOUNT","TRANSACTION_DATE"])

def Randomizer_TRANSACCIONES(num_registros_by_cajero_min,num_registros_by_cajero_max,num_practicajas,num_atm,month, year, DF_TRANSACCIONES):
    print("hELLO")
    tipo_transaccion = ["DEPOSITO","RETIRO"]
    monto_retiro = [x for x in range(100,9100,100)]

    if month in (1,3,5,7,8,10,12):
        month_day = [y for y in range(1,32,1)]
    elif month in(4,6,9,11):
        month_day = [y for y in range(1,31,1)]
    else:
        month_day = [y for y in range(1,28,1)]

    for x in range(num_atm):
        tipo_d = "DISPENSADOR"
        num_registros_by_cajero = random.randrange(num_registros_by_cajero_min,num_registros_by_cajero_max,1)

        for y in range(num_registros_by_cajero):
            temp_date = str(random.choice(month_day))+"/"+str(month)+"/"+str(year)
            temp_transaccion = tipo_transaccion[1]
            temp_monto_retiro = random.choice(monto_retiro)

            DF_TRANSACCIONES.loc[len(DF_TRANSACCIONES.index)] = [x,tipo_d,temp_date,temp_monto_retiro,temp_transaccion] 
            
            
    
    for x in range(num_practicajas):
        tipo_d = "PRACTDUAL"
        num_registros_by_cajero = random.randrange(num_registros_by_cajero_min,num_registros_by_cajero_max,1)

        for y in range(num_registros_by_cajero):
            temp_date = str(random.choice(month_day))+"/"+str(month)+"/"+str(year)
            temp_transaccion = random.choice(tipo_transaccion)
            temp_monto_retiro = random.choice(monto_retiro)

            DF_TRANSACCIONES.loc[len(DF_TRANSACCIONES.index)] = [x,tipo_d,temp_date,temp_monto_retiro,temp_transaccion] 

#Randomizar 09/2021 al 08/2022    

Randomizer_TRANSACCIONES(300,1500,5810,7972,3, 2021,DF_TRANSACCIONES)

#Randomizer_TRANSACCIONES(5,15,1,3,3, 2021,DF_TRANSACCIONES)

print(DF_TRANSACCIONES)
