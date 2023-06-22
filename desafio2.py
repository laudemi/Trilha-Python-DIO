# Desafio v.2
import textwrap


def menu():
    menu = """\n
    ================== MENU =====================
    [1] - Saque
    [2] - Depósito
    [3] - Extrato
    [4] - Novo Usuário
    [5] - Nova Conta
    [6] - Listar Contas
    [7] - Listar Usuários
    [0] - Sair
    ==============================================
    => """
    return input(textwrap.dedent(menu))


def sacar(*, saldo, valor_saque, extrato, limite, num_saque, limite_saques):
    saldo_excedido = valor_saque > saldo
    limite_excedido = valor_saque > limite
    saque_excedido = num_saque >= limite_saques

    if saldo_excedido:
        print("\n @@@ Operação falho! Você não tem saldo suficiente! @@@")

    elif limite_excedido:
        print("\n @@@ Operação falho! Limite de saque excedido! @@@")

    elif saque_excedido:
        print("\n @@@ Operação falho! Número máximo de saques excedido! @@@")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque:\t\tR$ {valor_saque:.2f}\n"
        num_saque += 1
        print('\n === Saque realizado com sucesso! ===')

    else:
        print("Operação falhou! Valor informado é inválido!")
    return saldo, extrato

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito:\tR$ {valor_deposito:.2f}\n"
        print('\n === Depósito realizado com sucesso! ===')
    else:
        print("\n @@@ Operação falhou! Valor informado é inválido! @@@")
    
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print("------- Extrato --------------")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print("")
    print("------------------------------")
    print(f"Saldo\t\tR$ {saldo:.2f}")
    print("------------------------------")
    return extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n @@@ Já existe usuário com esse CPF! @@@")
        return 
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd/mm/aaa): ")
    endereco = input("Informe o endereço (logradouro, numero, bairro, cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    
    print("---------- Usuário cadastrado com sucesso!' ----------------")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ==== Conta criada com sucesso! =====")
        return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}
    
    print("\n @@@ Usuário não encontrado, fluxo de criação de conta encerrado ! @@@")
    return None
 
 
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['num_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha = f"""\
            
            CPF: \t\t {usuario['cpf']}
            Titular:\t {usuario['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))        

def main():
    agencia = "0001"
    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    num_saque = 0
    limite_saques = 3
    extrato = ""

    while True:
    
        opcao = menu()

        if opcao == "1":
            valor_saque = float(input("Digite o valor a ser sacado: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor_saque = valor_saque,
                extrato = extrato,
                limite = limite,
                num_saque = num_saque,
                limite_saques = limite_saques,
            )
        elif opcao == "2":
            valor_deposito = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo,valor_deposito, extrato)
     
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            num_conta = len(contas) + 1
            conta = criar_conta(agencia, num_conta, usuarios)

            if conta:
                contas.append(conta)
        
        
        elif opcao == "6":
            listar_contas(contas)

        elif opcao =="7":
            listar_usuarios(usuarios)

        elif opcao == "0":
            break

        else:
            print("Opção Inválida, por favor tente novamente...")

main()