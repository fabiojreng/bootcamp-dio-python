class Usuario:
    @staticmethod
    def criar_usuario(nome: str, data_nascimento: str, cpf: str, endereco: str):
        return {
            "Nome": nome,
            "Data de NascimentO": data_nascimento,
            "CPF": cpf,
            "Endereço": endereco,
        }

    @staticmethod
    def filtrar_usuario(cpf: str, usuarios: list):
        for usuario in usuarios:
            if cpf == usuario["CPF"]:
                return usuario
