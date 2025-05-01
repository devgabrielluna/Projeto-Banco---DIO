saldo = 0  # Saldo inicial da conta
extrato = []  # Lista onde serão armazenadas as transações
numero_saques = 0  # Número de saques realizados
LIMITE_SAQUES = 3  # Limite de saques

# Função de depósito
def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor <= 0:
            print("Operação falhou! O valor informado deve ser maior que zero.")
        else:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f} | Saldo após depósito: R$ {saldo:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Operação falhou! Valor inválido. Por favor, insira um número válido.")
    
    return saldo, extrato

# Função de saque
def sacar(saldo, extrato, numero_saques):
    try:
        valor = float(input("Informe o valor do saque: R$ "))
        if valor <= 0:
            print("Operação falhou! O valor informado deve ser maior que zero.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        else:
            saldo -= valor
            extrato.append(f"Saque:    -R$ {valor:.2f} | Saldo após saque: R$ {saldo:.2f}")
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Operação falhou! Valor inválido. Por favor, insira um número válido.")
    
    return saldo, extrato, numero_saques

# Função para visualizar extrato
def ver_extrato(extrato, saldo):
    print("\n=============== EXTRATO ===============")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:  # Imprime cada item do extrato
            print(item)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=======================================")

# Loop principal
while True:
    # Exibe o menu diretamente
    print("""
    ================ MENU ================
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Sair
    =====================================
    """)

    # Captura a escolha do usuário
    escolha =input("Escolha uma opção: ")

    if escolha == "1":  # Depositar
        saldo, extrato = depositar(saldo, extrato)  # Chama a função depositar
    elif escolha == "2":  # Sacar
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)  # Chama a função sacar
    elif escolha == "3":  # Ver Extrato
        ver_extrato(extrato, saldo)  # Chama a função ver_extrato
    elif escolha == "4":  # Sair
        print("Programa Finalizado.")
        break
    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")