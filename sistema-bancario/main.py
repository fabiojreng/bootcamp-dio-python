from operacoes import Operacoes
from usuario import Usuario
from conta import ContaBancaria


def menu():
    return """
-------------- SISTEMA BANCÁRIO --------------

[D] DEPOSITO
[S] SAQUE
[E] EXTRATO
[NC] NOVA CONTA
[L] LISTAR CONTAS
[NU] NOVO USUÁRIO
[F] SAIR
"""


def main():
    operacoes = Operacoes()
    QTD_SAQUE: int = 3
    usuarios: list = []
    contas: list = []

    while True:
        case = input(menu())
        if case == "D":
            valor: float = float(input("Digite o valor: "))
            print(f"Status: {operacoes.depositar(valor)}\n")

        elif case == "S":
            if QTD_SAQUE < 0:
                print("Limite de saque atingido")
                break
            valor: float = float(input("Digite o valor: "))
            print(f"Status: {operacoes.sacar(valor=valor)}\n")
            QTD_SAQUE -= 1

        elif case == "E":
            print("Extrato:")
            operacoes.extrato()

        elif case == "NC":
            cpf = input("Digite o CPF: ")
            usuario = Usuario.filtrar_usuario(cpf, usuarios)
            if not usuario:
                print("Usuário não existe")
                break
            agencia = input("Digite a agencia: ")
            numero_conta = input("Digite o numero da conta: ")
            conta = ContaBancaria.criar_conta(agencia, numero_conta, usuario)
            contas.append(conta)
            print("Conta criada com sucesso")

        elif case == "L":
            print(
                "Não há contas"
                if not ContaBancaria.listar_contas(contas)
                else ContaBancaria.listar_contas(contas)
            )

        elif case == "NU":
            cpf = input("Digite o CPF: ")
            user_existe = Usuario.filtrar_usuario(cpf, usuarios)
            if user_existe:
                print("Usuário já existe")
                break
            nome = input("Digite o nome: ")
            data_nascimento = input("Digite a data de nascimento: ")
            endereco = input("Digite o endereço: ")
            usuario = Usuario.criar_usuario(nome, data_nascimento, cpf, endereco)
            usuarios.append(usuario)
            print("Usuário criado com sucesso")

        elif case == "F":
            print("Saindo...")
            break

        else:
            print("Operação inválida")
            break


main()
