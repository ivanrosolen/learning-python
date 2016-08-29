#!/usr/bin/python

def menu():

    saldo = 0
    end = False

    while end == False:
        option = input('Opcoes:\n1) Consultar Saldo\n2) Saque\n3) Deposito\nDigite a opcao desejada:')

        if option == 1:
            print 'Saldo atual: R$',saldo
        elif option == 2:
            valor_saque = input('Solicitado saque, digite o valor a ser sacado:')
            saldo = saldo - valor_saque
            print 'Saque ok, saldo atual: R$',saldo
        elif option == 3:
            valor_deposito = input('Solicitado deposito, digite o valor a ser depositado:')
            saldo = saldo + valor_deposito
            print 'Deposito ok, saldo atual: R$',saldo
        else:
            print 'Opcao Invalida'
            end = True

menu()