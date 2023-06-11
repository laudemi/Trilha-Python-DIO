menu = """

[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Sair

=> """

saldo = 0
limite = 500
qtde_saque = 0
limite_saques = 3
extrato = ""


while True:
   
    opcao = input(menu)

    if opcao == "1":
        valor_saque = float(input("Digite o valor a ser sacado: "))

        saldo_excedido = valor_saque > saldo
        limite_excedido = valor_saque > limite
        saque_excedido = qtde_saque >= limite_saques

        if saldo_excedido:
            print("Operação falho! Você não tem saldo suficiente!")

        elif limite_excedido:
            print("Operação falho! Limite de saque excedido!")

        elif saque_excedido:
            print("Operação falho! Número máximo de saques excedido!")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            qtde_saque += 1

        else:
            print("Operação falhou! Valor informado é inválido!")
        
    elif opcao == "2":
        print("Depósito")
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Operação falhou! Valor informado é inválido!")
        

    elif opcao == "3":

        print("------- Extrato --------------")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Seu saldo é de R$ {saldo:.2f}")
        print("------------------------------")

    elif opcao == "4":
        break

    else:
        print("Opção Inválida, por favor tente novamente...")
    