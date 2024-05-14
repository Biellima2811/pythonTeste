#Gabiel Levi Lima Rodrigues - Inicio do codigo
#Gabriel Levi Lima Rogures - Continuação
import random

#Lista para armazena os números das contas
contas = []

#Contador para cada conta criada
total_contas_criadas = 0

#Função teve que ser criada para diferenciar em objeto do outro.
def DB_Contas():
    print('=' * 10, ' Banco Facil - Base de Dados de Contas ', '=' * 10)
    print(total_contas_criadas)
    print('Contas Ativas: \n')
    for conta in contas:
        if conta.ativa:
            print('-' * 30)
            print(f'Nome do Titular: {conta.nome_completo}')
            print(f'Número da conta: {conta.numero_conta}')
            print(f'Saldo: R${conta.saldo:.2f}')
            print(f'Valores de Depositoz: R${conta.ocorrencias_deposito()}')
    print('=' * 37)
    print('Conta encerradas: ')
    for conta in contas:
        if not conta.ativa:
            print('-' * 30)
            print(f'Nome do Titular: {conta.nome_completo}')
            print(f'Número da conta: {conta.numero_conta}')
            print(f'Saldo: R${conta.saldo:.2f}')
            print(f'Valores de Deposito: R${conta.ocorrencias_deposito()}')
class Conta:
    #Construtor
    def __init__(self, nome_completo, cpf, telefone, endereco, email):
        global total_contas_criadas # Publica
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.numero_conta = random.randint(10000, 99999) #Gera uma numeração com 5 digitos
        self.saldo = float(0)
        self.ativa = True
        total_contas_criadas += 1
        self.depositos = []

    def depositar (self, valor):
        if conta.ativa:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Deposito de R${valor:.2f} realizado com sucesso!')
            print(f'Novo Saldo: R${self.consulta_saldo():.2f}')
        else:
            print('Não foi possivel fazer deposito. A conta está encerrada.')

    def ocorrencias_deposito(self):
        return self.depositos

    def sacar (self, valor):
        if self.ativa:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor:.2f} realizado com sucesso!')
                print(f'Novo Saldo: R$:{self.consulta_saldo():.2f}')
            else:
                print('Saldo insuficiente para realizar saque.')
        else:
            print('Não foi possisel saca o valor. A conta está encerrada.')

    def consulta_saldo (self):
        return self.saldo

    def encerra_conta(self):
        if self.saldo == 0:
            global total_contas_criadas
            self.ativa = False
            total_contas_criadas -= 1
            print('Conta encerrada com sucesso!')
        else:
            print('Não foi possivel encerra conta. O saldo deve está zerado!')
    def status_conta(self):
        if self.ativa:
            return 'Conta Ativa'
        else:
            return 'Conta não mais existente!'


'''---------------------------------------------------------------------'''
while True:
    #Menu de opçãoes
    print('=' * 10, '* Banco Facil *', '=' * 10)
    print('[1] - Abri Conta')
    print('[2] - Consulta Saldo')
    print('[3] - Deposito')
    print('[4] - Saque')
    print('[5] - Status da Conta')
    print('[6] - Encerramento de Conta', )
    print('[7] - BD_Contas')
    print('[8] - Sair')
    print('=' * 37)

    #Solicita ao usuario uma escolha.
    selec = input('Escolha uma das opções acima: ')

    #Condicionais possiveis de acordo com o menu.
    if selec == '1':
        print('*' * 5, 'Seja Bem-Vindo!', '*' * 5)
        print('Cadastro de Dados do Titular')

        # Validação de Nome completo
        while True:
            nome_completo = input('Nome Completo: ')
            if all(char.isalpha() or char.isspace() for char in nome_completo):
                break
            else:
                print('Por Favor, insira apenas caracteres no nome.')

        #Validação do Cpf
        while True:
            cpf = input('Cpf: ')
            if cpf.isdigit() and len(str(cpf)) == 11:
                break
            else:
                print('Por Favor, insira apenas 11 digitos numéricos no CPF')

        while True:
            telefone = input('Nº de Telefone: ')
            if telefone.isdigit() and len(str(telefone)) == 11:
                break
            else:
                print('Por Favor, insira apenas 11 digitos numéricos no Telefone')

        endereco = input('Endeço: ')
        email = input('E-mail: ')

        # Validação no nome completo, cpf, telefone, endereço e e-mail
        nova_conta = Conta(nome_completo, cpf, telefone, endereco, email)
        contas.append(nova_conta)

        print('*** Conta Criada com sucesso! ***')
        print(f'Número da Conta: {nova_conta.numero_conta}')

    elif selec == '2':
        #Condições possiveis no selec 2
        if not contas:
            print('Não há um conta criada. Por favor, abra uma conta primeio.')
        else:
            numero_conta = int(input('Informe o número da conta: '))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    print('-' * 30)
                    print('*** Dados do Titular ***')
                    print(f'Nome do Titula: {conta.nome_completo}')
                    print(f'Conta: {conta.numero_conta}')
                    if conta.ativa:
                        print(f'Saldo: R${conta.consulta_salto():.2f}')
                    else:
                        print('A conta está encerrada. Não é possivel visualizar o saldo. ')
                        break
            else:
                print('Numero de Conta invalido.')

    elif selec == '3':
        if not contas:
            print('Não há um conta criada. Por favor, abra uma conta primeio.')
        else:
            numero_conta = int(input('Informe o numero da conta: '))

            for conta in contas:
                if conta.numero_conta == numero_conta:
                    valor_deposito = float(input('Valor para deposito: R$'))
                    conta.depositar(valor_deposito)
                    break
            else:
                print('Numero de conta invalido.')


    elif selec == '4':
        if not contas:
            print('Não há uma conta criada. Por favor, abra uma conta primeiro.')
        else:
            numero_conta = int(input('Informe o número da conta: '))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    valor_saque = float(input('Valor para saque: R$'))
                    conta.sacar(valor_saque)
                    break
            else:
                print('Número de conta inválido.')

    elif selec == '5':
        if not contas:
            print('Não há um conta criada. Por favor, abra uma conta primeio.')
        else:
            numero_conta = int(input('Informe o número da conta: '))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    print('-' * 30)
                    print('*** Status da Conta ***')
                    print(conta.status_conta())
                    break
            else:
                print('Número de conta invalido.')
    elif selec == '6':
        if not contas:
            print('Não há um conta criada. Por favor, abra uma conta primeio.')
        else:
            numero_conta = int(input('Infome o número da conta: '))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    conta.encerra_conta()
                    break
            else:
                print('Número de conta invalido.')
    elif selec == '7':
        DB_Contas()
        print('\nDados Carregados....')
        print('Fim da consulta!')

    elif selec == '8':
        print('Encerrando programa...')
        break

    else:
        print('Opção Invalida! Por favor, escolha uma opção valida.')
#Gabriel Levi Lima Rodrigues - Edição final 30/03/2024 - 00:20
#Gabriel Levi Lima Rodrigues - Finalização do Codigo 30/03/2024 - 13:58