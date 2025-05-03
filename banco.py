import textwrap 
from datetime import datetime, timedelta

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe um usuário cadastrado com este CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro, Nº - Bairro - Cidade/Sigla Estado): ")
    
    usuario = {'cpf': cpf, 'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco}
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def menu():
    menu = """
    ================ MENU ================
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Nova Conta
        [5] - Listar Contas
        [6] - Novo Usuário
        [7] - Sair
    =======================================
    Digite sua escolha: 
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    try:
        if valor <= 0:
            print("Operação falhou! O valor informado deve ser maior que zero.")
        else:
            saldo += valor
            info_operacao = datetime.now().strftime("%d/%m/%Y %H:%M")
            extrato.append(f"Depósito: R$ {valor:.2f} | Saldo após depósito: R$ {saldo:.2f} | {info_operacao}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Operação falhou! Valor inválido. Por favor, insira um número válido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, numero_saques, limite_saques):
    try:
        if valor <= 0:
            print("Operação falhou! O valor informado deve ser maior que zero.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif numero_saques >= limite_saques:
            print("Quantidade de saques diários excedida.")
        else:
            info_operacao = datetime.now().strftime("%d/%m/%Y %H:%M")
            saldo -= valor
            extrato.append(f"Saque:    -R$ {valor:.2f} | Saldo após saque: R$ {saldo:.2f} | {info_operacao}")
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Operação falhou! Valor inválido. Por favor, insira um número válido.")
    
    return saldo, extrato, numero_saques

def ver_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=======================================")

def nova_conta(lista_contas, usuarios, agencia):
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        numero_conta = len(lista_contas) + 1
        nova_conta = {"cpf": cpf, "numero_conta": numero_conta, 'agencia': agencia}
        lista_contas.append(nova_conta)
        print(f"Conta número {numero_conta} - Agência: {agencia} criada com sucesso para o CPF {cpf}!")
    else:
        print("Usuário não encontrado!")

def listar_contas(lista_contas, usuarios):
    print("\n=============== CONTAS EXISTENTES ===============")
    if not lista_contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in lista_contas:
            
            usuario = filtrar_usuarios(conta['cpf'], usuarios)
            nome_titular = usuario['nome'] if usuario else "Desconhecido"
            
            linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{nome_titular}
            """
            print("=" * 50)
            print(textwrap.dedent(linha))
            print("=" * 50)
            
def main():
    AGENCIA = '0001'
    usuarios = []
    lista_contas = []
    saldo = 0  
    extrato = []  
    numero_saques = 0  
    LIMITE_SAQUES = 3  
    
    while True:
        escolha = menu()

        if escolha == "1": 
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato) 

        elif escolha == "2":  
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif escolha == "3":  
            ver_extrato(saldo, extrato=extrato) 

        elif escolha == "4":  
            nova_conta(lista_contas, usuarios, agencia=AGENCIA)

        elif escolha == "5":  
            listar_contas(lista_contas, usuarios)

        elif escolha == "6":  
            criar_usuario(usuarios)

        elif escolha == "7":  
            print("Programa Finalizado.")
            break

        else:
            print("Opção inválida! Por favor, selecione uma opção válida.")

main()