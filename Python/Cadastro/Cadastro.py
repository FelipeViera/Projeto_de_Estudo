import mysql.connector



def logar():
    escolha_03 = input('Continuar? S/N: ')
    if (escolha_03.upper() == 'N'):
        menu()

    conexao = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
    
    if conexao.is_connected():
        db_info = conexao.get_server_info()
        #print('Conectado ao banco de dados', db_info)
        cursor = conexao.cursor()

    email = input('Digite seu e-mail: ')
    senha = input('Digite sua senha: ')

    try:

        cursor.execute('SELECT senha from pessoas where email = %s' , (email,))
        simplificando = str(cursor.fetchone())
        simplificando = simplificando.replace('(', '')
        simplificando = simplificando.replace(')', '')
        simplificando = simplificando.replace(',', '')
        simplificando = simplificando.replace("'", '')
        simplificando = simplificando.replace("'", '')
        verificando = simplificando
              
        if (verificando == senha):
            print('Você logou')
            exibir(email)
        else:
            print('Sua senha está incorreta')
            logar()
            
    except:
        print('Não cadastrado')
        logar()
   

def mudar_cadastro(email):
    conexao = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
    
    if conexao.is_connected():
        db_info = conexao.get_server_info()
        #print('Conectado ao banco de dados', db_info)
        cursor = conexao.cursor()

    print('Digite')
    print('( 1 ) para mudar o nome')
    print('( 2 ) para mudar o cpf')
    print('( 3 ) para mudar a senha')
    print('( 4 ) para excluír o seu registro')
    escolha = input('Qual? ')
    
    
    if (escolha == '1'):
        mudanca = input('Digite o novo nome: ')
        cursor.execute('UPDATE pessoas SET nome = %s WHERE email = %s', (mudanca, email))
        conexao.commit()

    elif (escolha == '2'):
        mudanca = input('Digite o cpf: ')
        cursor.execute('UPDATE pessoas SET cpf = %s WHERE email = %s', (mudanca, email))
        conexao.commit()
    
    elif (escolha == '3'):
        mudanca = input('Digite a nova senha: ')
        cursor.execute('UPDATE pessoas SET senha = %s WHERE email = %s', (mudanca, email))
        conexao.commit()

    elif (escolha == '4'):
        pergunta = input('Tem certeza? S/N')
        if (pergunta.upper() == 'S'):
            cursor.execute('DELETE FROM pessoas WHERE email = %s', (email,))
            conexao.commit()
            menu()

        else:
            mudar_cadastro(email)
    else:
        mudar_cadastro(email)
    
    menu()


def exibir(email):
    conexao = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
    
    if conexao.is_connected():
        db_info = conexao.get_server_info()
        #print('Conectado ao banco de dados', db_info)
        cursor = conexao.cursor()
    
    cursor.execute('SELECT nome, email, cpf FROM pessoas where email = %s', (email,))
    print('Estes são seus dados de Nome, E-mail e CPF respectivamente')
    print(cursor.fetchone())
    resposta = input('Deseja modificar algum dado? S/N: ')
    if (resposta.upper() == 'S'):
        mudar_cadastro(email)
    else:
        menu()


def menu():
    print('Digite')
    print('( 1 ) Cadastrar')
    print('( 2 ) Logar')
    print('( 3 ) Saír')
    escolha = input('Qual? ')
    if (escolha == '1'):
        cadastrar()
    elif (escolha == '2'):
        logar()
    else:
        print('Encerrado')

def cadastrar():

    escolha_02 = input('Continuar? S/N: ')
    if (escolha_02.upper() == 'N'):
        menu()

    conexao = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
    
    if conexao.is_connected():
        db_info = conexao.get_server_info()
        #print('Conectado ao banco de dados', db_info)
        cursor = conexao.cursor()

    
    
    try:
        email = input('digite seu e-mail: ')
        cursor.execute('SELECT * FROM pessoas WHERE email = %s', (email,))
        resultado = cursor.fetchone()
        if (resultado):
            print('Este e-mail já está cadastrado')
            cadastrar()
        else:
             print('Não cadastrado')
             nome = str(input('Digite seu nome: '))
             senha = str(input('Digite uma senha: '))
             cpf = str(input('Digite seu cpf: '))
             cursor.execute('INSERT INTO pessoas(nome, email, cpf, senha) VALUES (%s, %s, %s, %s)', (nome, email, cpf, senha))
             conexao.commit()
             menu()


    except Exception as er:
        print('Não cadastrado')
        nome = str(input('Digite seu nome: '))
        senha = str(input('Digite uma senha: '))
        cpf = str(input('Digite seu cpf: '))
        cursor.execute('INSERT INTO pessoas(nome, email, cpf, senha) VALUES (%s, %s, %s, %s)', (nome, email, cpf, senha))
        conexao.commit()
        menu()

menu()
