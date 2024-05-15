class Operacoes:

    def __init__(self) -> None:
        self.__LIMITE_SAQUE: float = 500.0
        self.__saldo: float = 0
        self.__extrato_operacoes = []

    def depositar(self, valor: float) -> float | str:
        if valor < 0:
            return "Erro: Não é possível depositar valor negativo"
        self.__saldo += valor
        self.__extrato_operacoes.append(
            {"Operação": "Depositar", "Valor": f"R${valor}"}
        )
        return self.__saldo

    def sacar(self, valor: float) -> None:
        if valor < 0:
            return "Erro: Não é possível sacar valor negativo"
        if valor > self.__LIMITE_SAQUE:
            return "Erro: Limite de saque ultrapassado"
        if valor > self.__saldo:
            return "Erro: Saldo insuficiente"
        self.__saldo -= valor
        self.__extrato_operacoes.append({"Operação": "Sacar", "Valor": f"R${valor}"})
        return self.__saldo

    def extrato(self) -> list:
        return self.__extrato_operacoes

    def get_saldo(self) -> float:
        return self.__saldo
