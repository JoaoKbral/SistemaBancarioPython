

LIMITE_VALOR_SAQUE = 500
LIMITE_DIARIO_SAQUE = 3

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
        depositar(5000)

    elif opcao == "s":

    elif opcao == "e":

    elif opcao == "q":
        break

def depositar(valor):
    global saldo

    if valor > 0:
        saldo += valor


def sacar(valor):
    pass

def extrato():
    global extrato_deposito, extrato_saque

    for deposito in extrato_deposito:
        print(f"R$ {deposito}")

    for saque in extrato_saque:
        print(f"R$ {saque}")

