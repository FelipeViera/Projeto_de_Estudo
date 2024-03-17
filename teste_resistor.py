import random

faixa = [1, 2, 3, 4]

resposta = 0
#y = numero 
y = 10
# multiplicador
z = 0

resposta_min = 0
resposta_max = 0

cor = ["amarelo", "verde", "azul", "marrom"]



def faixa_01():
    global faixa
    faixa[0] = random.randint(0, 9)

    faixa_02()

def faixa_02():
    global faixa
    faixa[1] = random.randint(0, 9)

    multiplicador()

def multiplicador():
    global faixa
    faixa[2] = random.randint(0, 7)
    if (faixa[2] == 8 or faixa[2] == 9 ):
        multiplicador()
    else:

        tolerancia()

def tolerancia():
    global faixa
    faixa[3] = random.randint(1, 11)

    if (faixa[3] == 3 or faixa[3] == 4):
        tolerancia()
    else:
        if (faixa[3]== 9):
            tolerancia()
        else:
            conversao()

def conversao():
    global faixa
    global cor
    global y
    global z

    if faixa[0] == 0:
        cor[0] = "preto"
    elif faixa[0] == 1:
        cor[0] = "marrom"
    elif faixa[0] == 2:
        cor[0] = "vermelho"
    elif faixa[0] == 3:
        cor[0] = "laranja"
    elif faixa[0] == 4:
        cor[0] = "amarela"
    elif faixa[0] == 5:
        cor[0] = "verde"
    elif faixa[0] == 6:
        cor[0] = "azul"
    elif faixa[0] == 7:
        cor[0] = "violeta"
    elif faixa[0] == 8:
        cor[0] = "cinza"
    else:
        cor[0] = "branco"


    if faixa[1] == 0:
        cor[1] = "preto"
    elif faixa[1] == 1:
        cor[1] = "marrom"
    elif faixa[1] == 2:
        cor[1] = "vermelho"
    elif faixa[1] == 3:
        cor[1] = "laranja"
    elif faixa[1] == 4:
        cor[1] = "amarela"
    elif faixa[1] == 5:
        cor[1] = "verde"
    elif faixa[1] == 6:
        cor[1] = "azul"
    elif faixa[1] == 7:
        cor[1] = "violeta"
    elif faixa[1] == 8:
        cor[1] = "cinza"
    else:
        cor[1] = "branco"


    if faixa[2] == 0:
        cor[2] = "preto"
    elif faixa[2] == 1:
        cor[2] = "marrom"
    elif faixa[2] == 2:
        cor[2] = "vermelho"
    elif faixa[2] == 3:
        cor[2] = "laranja"
    elif faixa[2] == 4:
        cor[2] = "amarela"
    elif faixa[2] == 5:
        cor[2] = "verde"
    elif faixa[2] == 6:
        cor[2] = "azul"
    elif faixa[2] == 7:
        cor[2] = "violeta"
    elif faixa[2] == 10:
        cor[2] = "dourado"

    else:
        cor[0] = "prateado"



    if faixa[3]== 1:
        cor[3] = "marrom"
        z = 1
    elif faixa[3]== 2:
        cor[3] = "vermelho"
        z = 2
    elif faixa[3]== 5:
        cor[3] = "verde"
        z = 0.5
    elif faixa[3]== 6:
        cor[3] = "azul"
        z = 0.25
    elif faixa[3]== 7:
        cor[3] = "violeta"
        z = 0.1
    elif faixa[3]== 8:
        cor[3] = "cinza"
        z = 0.05
    elif faixa[3]== 10:
        cor[3] = "dourado"
        z = 5
    else:
        cor[3] = "prateado"
        z = 10

    responda()


def responda():
    global cor
    global faixa
    global resposta
    global resposta_min
    global resposta_max
    print("Quanta vale a resistência em ohms das seguintes faixas: ")
    resposta = int(input('cores na ordem: {}, {}, {} e {}  '.format(cor[0], cor[1], cor[2], cor[3])))

    resposta_min = int(input("Qual o minimo que o resistor deve medir? "))
    resposta_max = int(input("Qual o máximo que o resistor deve medir? "))
    verificar()



def verificar():
    global y
    global resposta
    global faixa
    global cor
    global z
    global resposta_min
    global resposta_max



    x = str(faixa[0]) + str(faixa[1])

    if (faixa[2] < 8):
        y = (y ** faixa[2])
    else:
        if (faixa[2] == 10):
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