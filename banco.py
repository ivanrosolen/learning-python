#!/usr/bin/python

def menu():

    saldo = 0.00
    cheque_especial = 100.00
    end = False

    while end == False:

        print 'SALDO ATUAL: R$ ',saldo

        option = input('Opcoes:\n1) Saque\n2) Deposito\nDigite a opcao desejada:')

        if option == 1:
            valor_saque = input('Solicitado saque, digite o valor a ser sacado:')

            diff = saldo - valor_saque;
            total = cheque_especial - valor_saque + saldo

            if  diff < 0 and total < 0:
                    print 'Saque maior do que o disponivel'
            else:
                saldo = saldo - valor_saque
                print 'Saque ok'
        elif option == 2:
            valor_deposito = input('Solicitado deposito, digite o valor a ser depositado:')
            saldo = saldo + valor_deposito
            print 'Deposito ok'
        else:
            print 'Opcao Invalida'
            end = True

menu()


