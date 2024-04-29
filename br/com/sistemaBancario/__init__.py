def depositar(saldo_depositar):
    valor = float(input("Insira um valor para depositar: "))
    flag = valida_depositar(valor_depositar=valor)
    if flag:
        saldo_depositar += valor
        return saldo_depositar
    else:
        pass # retornar algo para caso valor seja invalido


def valida_depositar(valor_depositar):
    if valor_depositar <= 0:
        return False
    else:
        return True


def sacar(*, saldo_sacar, extrato_sacar, numeros_saques):
    valor = float(input("Insira um valor para depositar: "))
    flag = valida_sacar(numeros_saques=numeros_saques, valor_valida_sacar=valor, v_saldo=saldo_sacar)


def valida_sacar(*, numeros_saques, valor_valida_sacar, v_saldo):
    LIMITE_VALOR_SAQUE = 500
    LIMITE_DIARIO_SAQUE = 3

    if numeros_saques == LIMITE_DIARIO_SAQUE:
        return False
    elif valor_valida_sacar <= 0 or valor_valida_sacar > LIMITE_VALOR_SAQUE:
        return False
    elif v_saldo < valor_valida_sacar:
        return False
    else:
        return True


def exibir_extrato(ext_deposito, ext_saque):
    for deposito in ext_deposito:
        print(f"R$ {deposito}")

    for saque in ext_saque:
        print(f"R$ {saque}")


MENU = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
extrato_deposito = []
extrato_saque = []

while True:

    opcao = input(MENU)

    if opcao == "d":
        pass

    elif opcao == "s":
        pass
        # sacar(wa)

    elif opcao == "e":
        pass

    elif opcao == "q":
        break

    else:
        print("Operação falhou! Opção invalida")

# criar usuario
# validar cadastro - cpfs diferentes
# armazera usuario em lista
# usuario de ter nome, data de nascimento, cpf, endereco(string no formato logradouro, numero - bairro - cidade/UF)
# conta: agencia, numero de conta usuario
# numero da conta é sequencial iniciando em 1
# numero da agencia é fixo, 0001
# usuario pode ter mais de uma conta, mas uma conta pertence a somente um usuario
