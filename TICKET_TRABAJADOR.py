import pandas as pd
import random 

DF_TICKET_TRABAJADOR = pd.DataFrame(columns=["TICKET_ID","TRABAJADOR_ID"])

issues_info = pd.read_csv("issues-raw.csv")

trabajador_info = pd.read_csv("TRABAJADORES/DF_TRABAJADORES.csv")

LISTA_DIVISIONES = ["BAJIO","METROPOLITANA NORTE","METROPOLITANA SUR","NORESTE","NOROESTE","OCCIDENTE","SUR","SURESTE","Occidente"]

def Randomizer_TICKET_TRABAJADOR(issues_info,trabajador_info,LISTA_DIVISIONES,DF_TICKET_TRABAJADOR):
    for x in LISTA_DIVISIONES:
        if x == "Occidente":
            temp_issues = issues_info[issues_info["division"] == "Occidente"]["ticket_id"]
            temp_trabajador = trabajador_info[trabajador_info["DIVISION"] == "OCCIDENTE"]["TRABAJADOR_ID"]
        else:
            temp_issues = issues_info[issues_info["division"] == x]["ticket_id"]
            temp_trabajador = trabajador_info[trabajador_info["DIVISION"] == x]["TRABAJADOR_ID"]

        for y in list(temp_issues):
            temp_select_trabajador = random.choice(list(temp_trabajador))

            DF_TICKET_TRABAJADOR.loc[len(DF_TICKET_TRABAJADOR.index)] = [y,temp_select_trabajador] 

Randomizer_TICKET_TRABAJADOR(issues_info,trabajador_info,LISTA_DIVISIONES,DF_TICKET_TRABAJADOR)
DF_TICKET_TRABAJADOR.to_csv("TICKETS_BY_WORKER/DF_TICKET_TRABAJADOR.csv")




