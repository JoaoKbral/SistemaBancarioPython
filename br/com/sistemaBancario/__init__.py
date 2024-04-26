menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f\n}"

        else:
            print("Operação falhou! Valor inválido")

    elif opcao == "s":
        if numero_saques == 3:
            print("Não é mais possível sacar hoje")
            continue

        valor = float(input("Informe o valor do saque: "))

        if valor > limite:
            print("Operação falhou! Excedeu o valor limite de saque")
            continue

        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente")
            continue

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f\n}"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
