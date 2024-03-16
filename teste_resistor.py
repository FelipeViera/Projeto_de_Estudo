import random

primeira_faixa = 0
segunda_faixa = 0
terceira_faixa = 0
quarta_faixa = 0
resposta = 0
y = 10
z = 0

resposta_min = 0
resposta_max = 0

primeira_cor = ""
segunda_cor = ""
terceira_cor = ""
quarta_cor = ""


def faixa_01():
    global primeira_faixa
    primeira_faixa = random.randint(0, 9)

    faixa_02()

def faixa_02():
    global segunda_faixa
    segunda_faixa = random.randint(0, 9)

    multiplicador()

def multiplicador():
    global terceira_faixa
    terceira_faixa = random.randint(0, 7)
    if (terceira_faixa == 8 or terceira_faixa == 9 ):
        multiplicador()
    else:

        tolerancia()

def tolerancia():
    global quarta_faixa
    quarta_faixa = random.randint(1, 11)

    if (quarta_faixa == 3 or quarta_faixa == 4):
        tolerancia()
    else:
        if (quarta_faixa == 9):
            tolerancia()
        else:
            conversao()

def conversao():
    global primeira_faixa
    global segunda_faixa
    global terceira_faixa
    global quarta_faixa
    global primeira_cor
    global segunda_cor
    global terceira_cor
    global quarta_cor
    global y
    global z

    if primeira_faixa == 0:
        primeira_cor = "preto"
    elif primeira_faixa == 1:
        primeira_cor = "marrom"
    elif primeira_faixa == 2:
        primeira_cor = "vermelho"
    elif primeira_faixa == 3:
        primeira_cor = "laranja"
    elif primeira_faixa == 4:
        primeira_cor = "amarela"
    elif primeira_faixa == 5:
        primeira_cor = "verde"
    elif primeira_faixa == 6:
        primeira_cor = "azul"
    elif primeira_faixa == 7:
        primeira_cor = "violeta"
    elif primeira_faixa == 8:
        primeira_cor = "cinza"
    else:
        primeira_cor = "branco"


    if segunda_faixa == 0:
        segunda_cor = "preto"
    elif segunda_faixa == 1:
        segunda_cor = "marrom"
    elif segunda_faixa == 2:
        segunda_cor = "vermelho"
    elif segunda_faixa == 3:
        segunda_cor = "laranja"
    elif segunda_faixa == 4:
        segunda_cor = "amarela"
    elif segunda_faixa == 5:
        segunda_cor = "verde"
    elif segunda_faixa == 6:
        segunda_cor = "azul"
    elif segunda_faixa == 7:
        segunda_cor = "violeta"
    elif segunda_faixa == 8:
        segunda_cor = "cinza"
    else:
        segunda_cor = "branco"


    if terceira_faixa == 0:
        terceira_cor = "preto"
    elif terceira_faixa == 1:
        terceira_cor = "marrom"
    elif terceira_faixa == 2:
        terceira_cor = "vermelho"
    elif terceira_faixa == 3:
        terceira_cor = "laranja"
    elif terceira_faixa == 4:
        terceira_cor = "amarela"
    elif terceira_faixa == 5:
        terceira_cor = "verde"
    elif terceira_faixa == 6:
        terceira_cor = "azul"
    elif terceira_faixa == 7:
        terceira_cor = "violeta"
    elif terceira_faixa == 10:
        terceira_cor = "dourado"

    else:
        primeira_cor = "prateado"



    if quarta_faixa == 1:
        quarta_cor = "marrom"
        z = 1
    elif quarta_faixa == 2:
        quarta_cor = "vermelho"
        z = 2
    elif quarta_faixa == 5:
        quarta_cor = "verde"
        z = 0.5
    elif quarta_faixa == 6:
        quarta_cor = "azul"
        z = 0.25
    elif quarta_faixa == 7:
        quarta_cor = "violeta"
        z = 0.1
    elif quarta_faixa == 8:
        quarta_cor = "cinza"
        z = 0.05
    elif quarta_faixa == 10:
        quarta_cor = "dourado"
        z = 5
    else:
        quarta_cor = "prateado"
        z = 10

    responda()


def responda():
    global resposta
    global resposta_min
    global resposta_max
    print("Quanta vale a resistência em ohms das seguintes faixas: ")
    resposta = int(input('cores na ordem: {}, {}, {} e {}  '.format(primeira_cor, segunda_cor, terceira_cor, quarta_cor)))

    resposta_min = int(input("Qual o minimo que o resistor deve medir? "))
    resposta_max = int(input("Qual o máximo que o resistor deve medir? "))
    verificar()



def verificar():
    global y
    global resposta
    global primeira_faixa
    global segunda_faixa
    global terceira_faixa
    global z
    global resposta_min
    global resposta_max



    x = str(primeira_faixa) + str(segunda_faixa)

    if (terceira_faixa < 8):
        y = (y ** terceira_faixa)
    else:
        if (terceira_faixa == 10):
            y = 0.1
        else:
            y = 0.01
    gabarito = int(x) * y

    minimo_gab = gabarito - ((z/100) * gabarito)
    max_gab = gabarito + ((z / 100) * gabarito)

    if (resposta == gabarito):
        print("você acertou o valor nominal")
        if (minimo_gab == resposta_min and max_gab == resposta_max):
            print("você acertou tudo!")
        else:
            print("Porém, precisa revisar seus estudos com a tolerância")



    else:
        print("errou")

    menu()


def menu():
    decisao = int(input("Digite 1 para iniciar novamente e 0 para fechar o app: "))
    if (decisao > 0):
        faixa_01()
    else:
        print('fim')



faixa_01()

