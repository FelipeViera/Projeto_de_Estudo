import random
import sqlite3



#conexão:

banco = sqlite3.connect('banco_de_dados/resistor.db')
cursor = banco.cursor()



#Código: 

faixa = [1, 2, 3, 4]

resposta = 0
valor_multiplicador = 10

percentual = 0

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
    global valor_multiplicador
    global percentual

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
        percentual = 1
    elif faixa[3]== 2:
        cor[3] = "vermelho"
        percentual = 2
    elif faixa[3]== 5:
        cor[3] = "verde"
        percentual = 0.5
    elif faixa[3]== 6:
        cor[3] = "azul"
        percentual = 0.25
    elif faixa[3]== 7:
        cor[3] = "violeta"
        percentual = 0.1
    elif faixa[3]== 8:
        cor[3] = "cinza"
        percentual = 0.05
    elif faixa[3]== 10:
        cor[3] = "dourado"
        percentual = 5
    else:
        cor[3] = "prateado"
        percentual = 10

    responda()


def responda():
    global cor
    global faixa
    global resposta
    global resposta_min
    global resposta_max
    print(' ')
    print("Quanto vale a resistência em ohms das seguintes faixas: ")
    resposta = int(input('cores na ordem: {}, {}, {} e {}  '.format(cor[0], cor[1], cor[2], cor[3])))

    resposta_min = int(input("Qual o minimo que o resistor deve medir? "))
    resposta_max = int(input("Qual o máximo que o resistor deve medir? "))
    verificar()



def verificar():
    global valor_multiplicador
    global resposta
    global faixa
    global cor
    global percentual
    global resposta_min
    global resposta_max



    numero = str(faixa[0]) + str(faixa[1])

    if (faixa[2] < 8):
        valor_multiplicador = (valor_multiplicador ** faixa[2])
    else:
        if (faixa[2] == 10):
            valor_multiplicador = 0.1
        else:
            valor_multiplicador = 0.01
    gabarito = int(numero) * valor_multiplicador

    minimo_gab = gabarito - ((percentual/100) * gabarito)
    max_gab = gabarito + ((percentual / 100) * gabarito)

    cursor.execute('UPDATE registro SET TENTATIVAS = TENTATIVAS + 1')
    banco.commit()

    if (resposta == gabarito):
        print("você acertou o valor nominal")

        cursor.execute('UPDATE registro SET ACERTOS_NOMINAIS = ACERTOS_NOMINAIS + 1')
        banco.commit()


        if (minimo_gab == resposta_min and max_gab == resposta_max):
            print("você acertou tudo!")

            cursor.execute('UPDATE registro SET ACERTOS = ACERTOS + 1')
            banco.commit()
            
        else:
            print("Porém, precisa revisar seus estudos com a tolerância")
            cursor.execute('UPDATE registro SET ERROS_DE_TOLERÂNCIA = ERROS_DE_TOLERÂNCIA + 1')
            banco.commit()



    else:
        print("errou")
        cursor.execute('UPDATE registro SET ERROS = ERROS + 1')
        banco.commit()

    
    mostrar_banco()
    


    

def mostrar_banco():
    print(' ')
    cursor.execute('SELECT TENTATIVAS FROM registro')

    simplificando = str(cursor.fetchone())
    simplificando = simplificando.replace('(', ' ')
    simplificando = simplificando.replace(')', ' ')
    simplificando = simplificando.replace(',', ' ')

    print('Número de tentativas: {}'.format(simplificando))

    cursor.execute('SELECT ACERTOS_NOMINAIS FROM registro')

    simplificando = str(cursor.fetchone())
    simplificando = simplificando.replace('(', ' ')
    simplificando = simplificando.replace(')', ' ')
    simplificando = simplificando.replace(',', ' ')

    print('Número de acertos nominais: {}'.format(simplificando))

    cursor.execute('SELECT ACERTOS FROM registro')

    simplificando = str(cursor.fetchone())
    simplificando = simplificando.replace('(', ' ')
    simplificando = simplificando.replace(')', ' ')
    simplificando = simplificando.replace(',', ' ')

    print('Número de acertos: {}'.format(simplificando))

    cursor.execute('SELECT ERROS FROM registro')

    simplificando = str(cursor.fetchone())
    simplificando = simplificando.replace('(', ' ')
    simplificando = simplificando.replace(')', ' ')
    simplificando = simplificando.replace(',', ' ')

    print('Número de erros: {}'.format(simplificando))

    
    cursor.execute('SELECT ERROS_DE_TOLERÂNCIA FROM registro')

    simplificando = str(cursor.fetchone())
    simplificando = simplificando.replace('(', ' ')
    simplificando = simplificando.replace(')', ' ')
    simplificando = simplificando.replace(',', ' ')

    print('Número de erros nominais: {}'.format(simplificando))
    menu()

def menu():

    
    decisao = int(input("Digite 1 para iniciar novamente e 0 para fechar o app: "))
    if (decisao > 0):
        faixa_01()
    else:
        print('fim')



faixa_01()