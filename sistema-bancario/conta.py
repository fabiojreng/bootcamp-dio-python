class ContaBancaria:
    @staticmethod
    def criar_conta(agencia: str, numero_conta: str, usuario: dict):
        return {
            "Agencia": agencia,
            "Número da conta": numero_conta,
            "Usuário": usuario,
        }

    @staticmethod
    def listar_contas(contas: list):
        dados: list = []
        for conta in contas:
            dados.append(
                f"Agência:{conta['Agencia']}, Conta:{conta['Número da conta']}, Titular:{conta['Usuário']['Nome']}"
            )
        return dados
