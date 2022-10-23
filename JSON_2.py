import json

f = open('data_2.json')

data = json.load(f)

diccionario = dict()

lista = []
lista_name = []

for x in range(len(data)):
    
    if lista_name == []:
        diccionario['name'] = data[x]['name']
        diccionario['data'] = [{'name': data[x]['name_1'],'value': int(data[x]['value'])}]
        lista_name.append(data[x]['name'])


    elif data[x]['name'] not in lista_name:
        lista.append(diccionario)
        diccionario = {}
        diccionario['name'] = data[x]['name']
        diccionario['data'] = [{'name': data[x]['name_1'],'value': int(data[x]['value'])}]
        lista_name.append(data[x]['name'])


    else:
        diccionario['data'].append({'name': data[x]['name_1'],'value': int(data[x]['value'])})
lista.append(diccionario)


print(str(lista).replace("'name'","name").replace("'value'","value").replace("'data'","data"))
