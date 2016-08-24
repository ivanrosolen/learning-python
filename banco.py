#!/usr/bin/python

def menu():

    saldo = 150
    end = False

    while end == False:
        option = input('Opcoes:\n1) Consultar Saldo\n2) Saque\n3) Deposito\nDigite a opcao desejada:')

        if option == 1:
            print 'Saldo atual: R$',saldo
        elif option == 2:
            print 'Solicitar o saque'
        elif option == 3:
            print 'Solicitar o deposito'
        else:
            print 'Opcao Invalida'
            end = True

menu()