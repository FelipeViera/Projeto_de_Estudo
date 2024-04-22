import requests
import json

link2 = "http://viacep.com.br/ws/RS/AlvoradA/Rua Doutor João Inácio/json/"
lugar = requests.get(link2)
lugar = lugar.json()
print(lugar)