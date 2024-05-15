from operacoes import Operacoes

MENU = """
-------------- SISTEMA BANCÁRIO --------------

[D] DEPOSITO
[S] SAQUE
[E] EXTRATO
[F] SAIR
"""
operacoes = Operacoes()
QTD_SAQUE: int = 3

while True:
    case = input(MENU)
    if case == "D":
        valor: float = float(input("Digite o valor: "))
        print("\n--------------------------------------")
        print("Depositando...")
        print(f"Status: {operacoes.depositar(valor)}\n")
        print("--------------------------------------")

    elif case == "S":
        if QTD_SAQUE < 0:
            print("Limite de saque atingido")
            break
        valor: float = float(input("Digite o valor: "))
        print("\n--------------------------------------")
        print("Sacando...")
        print(f"Status: {operacoes.sacar(valor)}\n")
        print("--------------------------------------")
        QTD_SAQUE -= 1

    elif case == "E":
        print("\n--------------------------------------")
        print("Extrato:")
        print(
            "Sem movimentações feitas"
            if not operacoes.extrato()
            else operacoes.extrato()
        )
        print(f"Saldo: {operacoes.get_saldo()}")
        print("--------------------------------------")

    elif case == "F":
        print("\n--------------------------------------")
        print("Saindo")
        break

    else:
        print("Operação inválida")
        break
