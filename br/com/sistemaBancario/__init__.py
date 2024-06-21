import textwrap


def menu():
    opcoes = """

    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\tExtrato
    [lc]\tListar contas
    [nc]\tNova conta
    [nu]\tNovo usuário
    [q]\t\tSair

    => """

    return input(textwrap.dedent(opcoes))


def depositar(depositar_saldo, depositar_valor, extrato, /):
    flag = valida_depositar(valida_depositar_valor=depositar_valor)
    if flag:
        depositar_saldo += depositar_valor
        extrato += f"Depósito: R$ {depositar_valor:,.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n @@@ Operação falhou! O valor é inválido @@@")

    return depositar_saldo, extrato


def valida_depositar(valida_depositar_valor):
    if valida_depositar_valor <= 0:
        return False
    else:
        return True


def sacar(*, saldo, valor, extrato, numeros_saques, limite, limite_diario_saque):
    flag = valida_sacar(numeros_saques=numeros_saques, valor=valor,
                        saldo=saldo, limite=limite, limite_diario_saque=limite_diario_saque)
    if flag:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numeros_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    return [saldo, extrato, numeros_saques]


def valida_sacar(*, numeros_saques, valor, saldo, limite,
                 limite_diario_saque):
    if numeros_saques == limite_diario_saque:
        print("\n@@@ Operação falhou! Limite diário atingido @@@")
        return False

    elif valor <= 0 or valor > limite:
        print("\n@@@ Operação falhou! Valor menor que 0 ou maior que o limite @@@")
        return False

    elif saldo < valor:
        print("\n@@@ Operação falhou! Saldo insuficiente @@@")
        return False

    else:
        return True


def exibir_extrato(saldo, /, *, extrato):

    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.f}")


def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente números): ")
    usuario = validar_cpf(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    })

    print("\n=== Usuário cadastrado com sucesso! ===")


def validar_cpf(cpf, usuarios):
    # usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    # return usuarios_filtrado if usuario_filtrado else None
    for usuario in usuarios:
        if usuario.get("cpf") == cpf:

            return usuario

    return None


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o cpf do usuário (somente números): ")
    usuario = validar_cpf(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        return

    print("\n @@@ Usuário não encontrado @@@")


def listar_contas(contas):
    print("\n\n")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE = 500
    LIMITE_DIARIO_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0.0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Insira um valor para depositar: "))
            saldo, extrato_deposito = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Insira um valor para sacar: "))

            saldo, extrato_saque, numero_saques = sacar(saldo=saldo, extrato=extrato,
                                                        valor=valor, numeros_saques=numero_saques,
                                                        limite_diario_saque=LIMITE_DIARIO_SAQUE, limite=LIMITE)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nc":
            criar_conta(agencia=AGENCIA, numero_conta=numero_conta, usuarios=usuarios, contas=contas)
            if len(contas) == numero_conta:
                numero_conta += 1

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação falhou! Opção invalida")


main()
# criar usuario
# validar cadastro - cpfs diferentes
# armazera usuario em lista
# usuario de ter nome, data de nascimento, cpf, endereco(string no formato logradouro, numero - bairro - cidade/UF)
# conta: agencia, numero de conta usuario
# numero da conta é sequencial iniciando em 1
# numero da agencia é fixo, 0001
# usuario pode ter mais de uma conta, mas uma conta pertence a somente um usuario
