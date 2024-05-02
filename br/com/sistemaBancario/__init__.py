def menu():
    opcoes = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    saldo = 0.0
    extrato_deposito = ""
    extrato_saque = ""
    numero_saques = 0

    while True:

        opcao = input(opcoes)

        if opcao == "d":
            valor = float(input("Insira um valor para depositar: "))
            saldo, extrato_deposito = depositar(depositar_saldo=saldo, depositar_valor=valor,
                                                depositar_extrato=extrato_deposito)

        elif opcao == "s":
            valor = float(input("Insira um valor para sacar: "))
            saldo, extrato_saque, numero_saques = sacar(sacar_saldo=saldo, sacar_extrato=extrato_saque, sacar_valor=valor,
                                         sacar_numeros_saques=numero_saques)

        elif opcao == "e":
            exibir_extrato(exibir_extrato_deposito=extrato_deposito, exibir_extrato_saque=extrato_saque)

        elif opcao == "q":
            break

        else:
            print("Operação falhou! Opção invalida")


def depositar(depositar_saldo, depositar_valor, depositar_extrato):
    flag = valida_depositar(valida_depositar_valor= depositar_valor)
    if flag:
        depositar_saldo += depositar_valor
        depositar_extrato += f"Depósito: R$ {depositar_valor:,.2f}\n"
    return [depositar_saldo, depositar_extrato]


def valida_depositar(valida_depositar_valor):
    if valida_depositar_valor <= 0:
        print("Operação falhou! Valor menor que 0")
        return False
    else:
        return True


def sacar(*, sacar_saldo, sacar_valor, sacar_extrato, sacar_numeros_saques):

    flag = valida_sacar(valida_sacar_numeros_saques=sacar_numeros_saques, valida_sacar_valor=sacar_valor,
                        valida_sacar_saldo=sacar_saldo)
    if flag:
        sacar_saldo -= sacar_valor
        sacar_extrato += f"Saque: R$ {sacar_valor:.2f}\n"
        sacar_numeros_saques += 1
    return [sacar_saldo, sacar_extrato, sacar_numeros_saques]


def valida_sacar(*, valida_sacar_numeros_saques, valida_sacar_valor, valida_sacar_saldo):
    limite_valor_saque = 500
    limite_diario_saque = 3

    if valida_sacar_numeros_saques == limite_diario_saque:
        print("Operação falhou! Limite diário atingido")
        return False

    elif valida_sacar_valor <= 0 or valida_sacar_valor > limite_valor_saque:
        print("Operação falhou! Valor menor que 0 ou maior que o limite")
        return False

    elif valida_sacar_saldo < valida_sacar_valor:
        print("Operação falhou! Saldo insuficiente")
        return False

    else:
        return True


def exibir_extrato(exibir_extrato_deposito, exibir_extrato_saque):
    print(exibir_extrato_deposito)
    print(exibir_extrato_saque)


menu()
# criar usuario
# validar cadastro - cpfs diferentes
# armazera usuario em lista
# usuario de ter nome, data de nascimento, cpf, endereco(string no formato logradouro, numero - bairro - cidade/UF)
# conta: agencia, numero de conta usuario
# numero da conta é sequencial iniciando em 1
# numero da agencia é fixo, 0001
# usuario pode ter mais de uma conta, mas uma conta pertence a somente um usuario
