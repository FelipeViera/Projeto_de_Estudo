import requests
import json




def menu():
    try: solicitacao_api()
    except:
        print("Você digitou de maneira incorreta. Tente Novamente")
        menu()


def solicitacao_api():
    link = "https://economia.awesomeapi.com.br/last/USD-BRL"
    cotacoes = requests.get(link)
    cotacoes = cotacoes.json()
    cotacao_dollar = cotacoes['USDBRL']["bid"]
    cotacao_dollar = float(cotacao_dollar)
    inicio(cotacao_dollar)

def inicio(cotacao_dollar):
    print("Olá, este programa tem a finalidade de converter um valor em real para dólar  e virse versa")
    print('(1) Quero converter real em dólar')
    print('(2) Quero converter dólar em real')
    resposta = input('Digite: ').strip()
    resposta = str(resposta)
    if (resposta == 1):
        real_to_dolar(cotacao_dollar)
    else:
        dolar_to_real(cotacao_dollar)

def real_to_dolar(cotacao_dollar):
    valor = input("Digite: R$").strip()
    valor = valor.replace(',','.')
    valor = float(valor)
    valor_em_dollar = round(valor/cotacao_dollar, 2)
    valor_em_dollar = str(valor_em_dollar)
    valor_em_dollar = valor_em_dollar.replace('.', ',')
    print("A quantia que você tem em reais equivale a US$ {}".format(valor_em_dollar))

def dolar_to_real(cotacao_dollar):
    valor = input("Digite: US$").strip()
    valor = valor.replace(',','.')
    valor = float(valor)
    valor_em_real = round(valor * cotacao_dollar, 2)
    valor_em_real = str(valor_em_real)
    valor_em_real = valor_em_real.replace('.', ',')
    print("A quantia que você tem em US$ equivale a R$ {}".format(valor_em_real))

menu()