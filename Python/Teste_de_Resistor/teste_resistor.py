import random
import mysql.connector



#conexão:


conexao = mysql.connector.connect(host='localhost', database='teste_resistor', user='root', password='')
    
if conexao.is_connected():
    cursor = conexao.cursor()


def faixa_01():

    try:
        faixa = [1, 2, 3, 4]
        faixa[0] = random.randint(0, 9)
        faixa_02(faixa)
    except:
        print("houve um erro")
        print("Tente digitar corretamente os valores")
        cursor.close()


def faixa_02(faixa):
    faixa[1] = random.randint(0, 9)
    multiplicador(faixa)

def multiplicador(faixa):
    faixa[2] = random.randint(0, 7)
    if (faixa[2] == 8 or faixa[2] == 9 ):
        multiplicador(faixa)
    else:
        tolerancia(faixa)

def tolerancia(faixa):
    faixa[3] = random.randint(1, 11)

    if (faixa[3] == 3 or faixa[3] == 4):
        tolerancia(faixa)
    else:
        if (faixa[3]== 9):
            tolerancia(faixa)
        else:
            conversao(faixa)

def conversao(faixa):

    cor = ["amarelo", "verde", "azul", "marrom"]

    cursor.execute("SELECT COR FROM CODIGO_CORES WHERE ID = %s",(faixa[0],))
    simplificando = str(cursor.fetchone())
    simplificando = simplificando.replace('(', '')
    simplificando = simplificando.replace(')', '')
    simplificando = simplificando.replace(',', '')
    simplificando = simplificando.replace("'", '')

    cor[0] = simplificando


    cursor.execute("SELECT COR FROM CODIGO_CORES WHERE ID = %s",(faixa[1],))
    simplificando = str(cursor.fetchone())
    simplificando = simplificando.replace('(', '')
    simplificando = simplificando.replace(')', '')
    simplificando = simplificando.replace(',', '')
    simplificando = simplificando.replace("'", '')
    cor[1] = simplificando


    cursor.execute("SELECT COR FROM CODIGO_CORES WHERE ID = %s",(faixa[2],))
    simplificando = str(cursor.fetchone())
    simplificando = simplificando.replace('(', '')
    simplificando = simplificando.replace(')', '')
    simplificando = simplificando.replace(',', '')
    simplificando = simplificando.replace("'", '')
    cor[2] = simplificando


    cursor.execute("SELECT COR FROM CODIGO_CORES WHERE ID = %s",(faixa[3],))
    simplificando = str(cursor.fetchone())
    simplificando = simplificando.replace('(', '')
    simplificando = simplificando.replace(')', '')
    simplificando = simplificando.replace(',', '')
    simplificando = simplificando.replace("'", '')
    cor[3] = simplificando


    responda(faixa, cor)


def responda(faixa, cor):

   
    print(' ')
    print("Quanto vale a resistência em ohms das seguintes faixas: ")
    resposta = input('cores na ordem: {}, {}, {} e {}: '.format(cor[0], cor[1], cor[2], cor[3])).strip()
    resposta = int(resposta)
    resposta_min = input("Qual o minimo que o resistor deve medir? ").strip()
    resposta_max = input("Qual o máximo que o resistor deve medir? ").strip()
    resposta_max = float(resposta_max)
    resposta_min = float(resposta_min)

    verificar(faixa, resposta, resposta_max, resposta_min)

def verificar(faixa, resposta, resposta_max, resposta_min):


    cursor.execute("SELECT TOLERANCIA FROM CODIGO_CORES WHERE ID = %s",(faixa[2],))
    simplificando = str(cursor.fetchone())
    simplificando = simplificando.replace('(', ' ')
    simplificando = simplificando.replace(')', ' ')
    simplificando = simplificando.replace(',', ' ')
    percentual = float(simplificando)


    numero = str(faixa[0]) + str(faixa[1])

    if (faixa[2] < 8):
        valor_multiplicador = (10 ** faixa[2])
    else:
        if (faixa[2] == 10):
            valor_multiplicador = 0.1
        else:
            valor_multiplicador = 0.01
    gabarito = int(numero) * valor_multiplicador

    minimo_gab = gabarito - ((percentual/100) * gabarito)
    max_gab = gabarito + ((percentual / 100) * gabarito)

    minimo_gab = round(minimo_gab, 2)
    max_gab = round(max_gab, 2)

    cursor.execute('UPDATE registro SET TENTATIVAS = TENTATIVAS + 1')
    conexao.commit()

    if (resposta == gabarito):
        print("você acertou o valor nominal")

        cursor.execute('UPDATE registro SET ACERTOS_NOMINAIS = ACERTOS_NOMINAIS + 1')
        conexao.commit()


        if (minimo_gab == resposta_min and max_gab == resposta_max):
            print("você acertou tudo!")

            cursor.execute('UPDATE registro SET ACERTOS = ACERTOS + 1')
            conexao.commit()
            
        else:
            print("Porém, precisa revisar seus estudos com a tolerância")
            cursor.execute('UPDATE registro SET ERROS_DE_TOLERÂNCIA = ERROS_DE_TOLERÂNCIA + 1')
            conexao.commit()



    else:
        print("errou")
        cursor.execute('UPDATE registro SET ERROS = ERROS + 1')
        conexao.commit()

   
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

    print('Número de erros de tolerância: {}'.format(simplificando))
    menu()

def menu():

    
    decisao = int(input("Digite 1 para iniciar novamente e 0 para fechar o app: "))
    if (decisao > 0):
        faixa_01()
    else:
        print('fim')
        cursor.close()


faixa_01()