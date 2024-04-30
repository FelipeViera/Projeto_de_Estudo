#Este projeto consumirá uma API púlica de CEP
import requests
import json

def menu():
    print("Programa inicializado")
    print(" ")
    print("(1) Através do seu CEP achamos seu endereço")
    print("(2) Através do seu endereço achamos o seu cep")
    resposta = input("Digite: ").strip()

    try:        
        informacao_cep(resposta)

    except:
        print("Opa parece que você digitou alguma informação de maneira incorreta. Tente novamente")
        menu()
    

def solicitação_api(cep, resposta):

    link = "http://viacep.com.br/ws/{}/json/".format(cep)

    lugar = requests.get(link)
    lugar = lugar.json()

    if resposta == "1":
        uf = lugar["uf"]
        cidade = lugar["localidade"]
        logradouro = lugar["logradouro"]
        print("Seu estado: {}".format(uf))
        print("Sua cidade: {}".format(cidade))
        print("Sua rua/avenida: {}".format(logradouro))
        print(lugar)
    
    else:
        cod = lugar[0]['cep']
        print("Seu cep é {}".format(cod))
      

def informacao_cep(resposta):
    if resposta == "1":
        cep = input('Digite seu CEP: ').strip()
    else:
        uf = input("Digite seu UF: ").strip()
        uf = uf.upper()
        cidade = input("Digite o nome da sua cidade: ").strip()
        rua = input("Digite o nome da rua/avenida: ")
        cep = uf + "/" + cidade + "/" + rua
        
    solicitação_api(cep, resposta)


menu()