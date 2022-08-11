import time
import pyautogui as pa

movies = {"assistidos": ["0 - After"], "assistir": ['0 - Barraca do beijo'], 'alugados':['0 - Piranha 2', '1 - Todo mundo em pânico', '2 - Barbie'] }
alugar = ['0 - Thor', '1 - O Poderoso Chefão 2', '2 - Shrek 2']
clientes = {'Roberto': [' 0 - Avengers 2', '1 - Homem aranha 3'], 'Nathalia': ['0 - Barbie 2', '1 - Shrek 3']}

login=input('Digite seu login ("ADM, Cliente, Atendente): ').upper()
password=input('Digite a senha correspondente: ')

adm_password='Adm123456@'
cliente_password='Cliente123@'
atendente_password='Atendente123@'

#while login != "ADM" and "CLIENTE" and "ATENDENTE":
#    login = input('login invalido, favor insira novamente: ').upper()
#    password = input('Digite a senha: ')

if login=='ADM' and password != adm_password:
    print('login error')
    quit()
elif login=='CLIENTE' and password != cliente_password:
    print('login error')
    quit()
elif login=='ATENDENTE' and password != atendente_password:
    print('login error')
    quit()
elif login=='ADM' and password == adm_password:
    print('login successfully')
    time.sleep(2)
    programa_iniciar = "S"
    print('Iniciando o programa...')
    print('Iniciado com sucesso')
    print('Bem vindo administrador')
    while programa_iniciar == 'S':
        funcao=input('\n\nO que deseja realizar\n1 - Validar locação\n2- Devolver locação de cliente\n3 - Excluir locação\n4 - Fechar o programa: ')
        if funcao == '1':
            nome_cliente = input('Digite o nome do cliente que deseja validar as locações: ')
            if clientes.get(nome_cliente) != None:
                tmp_client=clientes[nome_cliente]
                print(tmp_client)
                time.sleep(2)
            else:
                print('cliente inexistente')
        elif funcao == '2':
            nome_cliente=input('Digite o nome do cliente que deseja alterar as locações: ')
            if clientes[nome_cliente] != None: 
                tmp_value=clientes.get(nome_cliente)
                valor=int(input('Digite a posição que deseja alterar: '))
                tmp_value[valor] = input('Digite o novo filmes do usuário: ')
                time.sleep(2)
            else:
                print('Usuário inexistente')
        elif funcao == '3':
            nome_cliente=input('Digite o nome do cliente que deseja excluir os valores: ')
            if clientes[nome_cliente] != None:
                valor = int(input('Digite a posição que deseja excluir'))
                tmp_value=clientes.get(nome_cliente)
                del tmp_value[valor]
                time.sleep(2)
            else: 
                print('Usuário inexistente')
        elif funcao == '4':
            quit()
elif login == 'CLIENTE' and password == cliente_password:
    print('login successfully')
    time.sleep(2)
    programa_iniciar = "S"
    print('Iniciando o programa...')
    print('Iniciado com sucesso')
    print('Bem vindo administrador')
    while programa_iniciar == 'S':
        funcao=input('Digite a função que deseja realizar:\n1 - Locar um filme\n2 - Visualizar assistidos\n3 - Assistir:\n 4 - Fechar o programa: ')
        if funcao == '1':
            print("Filmes disponiveis: ", alugar)
            movies[assistir]: input('Digite o nome do filme que deseja alugar: ')
            print('Filme cadastrado com sucesso')
            print(movies)
            time.sleep(2)
        elif funcao == '2':
            assistidos = 'assistidos'
            tmp_value2=movies.get(assistidos)
            print(tmp_value2)
            time.sleep(2)
        elif funcao == '3':
            print(movies)
            nome_filme = input('Insira o nome do filme que deseja assistir: ')
            print('Filme selecionado')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(1)
            print('Filme iniciando...')
            pa.press('win')
            pa.write('netflix')
            pa.press('enter')
            quit()
        elif funcao == '4':
            quit()
elif login == 'ATENDENTE' and password == atendente_password:
    programa_iniciar = 'S'
    while programa_iniciar == 'S':
        funcao=input('Digite a função que deseja:\n1 - Devolver uma locação\n2 - excluir filme\n3 - sair do programa: ')
        if funcao == '1':
            nome_cliente=input('Digite o nome do cliente que deseja alterar as locações: ')
            if clientes[nome_cliente] != None: 
                tmp_value=clientes.get(nome_cliente)
                valor=int(input('Digite a posição que deseja alterar: '))
                tmp_value[valor] = input('Digite o novo filmes do usuário: ')
                time.sleep(2)
        elif funcao == '2':
            nome_cliente=input('Digite o nome do cliente que deseja excluir os valores: ')
            if clientes[nome_cliente] != None:
                valor = input('Digite a posição que deseja excluir')
                tmp_value5=clientes.get(nome_cliente)
                del tmp_value5[valor]
                time.sleep(2)
        elif funcao == 3:
            quit()