import time
import random
funcionario = []
tot_fun_cadastrado = 0

class cadastro:
    #Construtor
    def __init__(self, nome_completo, cpf, telefone, endereco):
        global tot_fun_cadastrado #public
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.ativo = True
        self.matricula = random.randint(00000, 99999) #gera um numero de matricula aletorio de 5 digitos
        tot_fun_cadastrado += 1

while True:
    # Obtemos a hora atual em formato de tupla
    hora_atual = time.localtime()

    # Extrai a hora, minutos e segundos
    hora = hora_atual.tm_hour
    minutos = hora_atual.tm_min
    segundos = hora_atual.tm_sec

    # Exibe a hora formatada
    print(f"{hora:02}:{minutos:02}:{segundos:02}", end="", flush=True)

    # Aguarda 1 segundo antes de exibir a próxima atualização
    time.sleep(1)
    # Limpa a linha para atualização
    print("\r", end="")

    # Menu de opçãoes
    print('=' * 10, '* Relogio de Ponto *', '=' * 10)
    print('[1] - Cadastra Funcionario')
    print('[2] - Banco de Horas')
    print('[3] - Lista de Funcionarios')
    print('[4] - DataBase - Funcionarios')
    print('[5] - Status do Funcionario')
    print('[6] - Sair')
    print('=' * 37)

    # Extrai a hora, minutos e segundos
    hora = hora_atual.tm_hour
    minutos = hora_atual.tm_min
    segundos = hora_atual.tm_sec

    # Exibe a hora formatada
    print(f"{hora:02}:{minutos:02}:{segundos:02}", end="", flush=True)

    # Aguarda 1 segundo antes de exibir a próxima atualização
    time.sleep(1)
    # Limpa a linha para atualização
    print("\r", end="")

    opcao = input('Selecione a opção de acordo com a tela: ')
    hora_atual = time.localtime()


    if opcao == '1':

        #Validação do nome
        while True:
            print('*' * 5, 'Bem-Vindo', '*' * 5) # Tela de boas vindas para o cadastro
            print('Insira os dados como é solicitado, por favor!')
            nome_completo = input('Nome completo:')
            if all(char.isalpha() or char.isspace() for char in nome_completo):
                break #Condição para evitar erros de digitação
            else:
                print('Por favor, insira apenas caracteres no nome ! ')

        while True:
            cpf = input('Cpf: ')
            if cpf.isdigit() and len(str(cpf)) == 11:
                break #Condição para evitar erros de digitação
            else:
                print('Por favor, insira apenas 11 digitos numericos no CPF')

        while True:
            telefone = input('Nº de tele: ')
            if telefone.isdigit() and len(str(telefone)) == 11:
                break #Condição para evitar erros de digitação
            else:
                print('Por favor, insira apenas 11 digitos numeros no Telefone')

        endereco = input('Endereço - (ex:Rua abc, N123) : ')
        email = input('E-mail: (ex:seuemail@gmail.com)')

        ct_fucion = cadastro(nome_completo, cpf, telefone, endereco, email)
        cadastro.append(ct_fucion)

        print('*** Funcionario cadastrado com sucesso!! ***')
        print(f'Matricula: {ct_fucion.matricula}')
