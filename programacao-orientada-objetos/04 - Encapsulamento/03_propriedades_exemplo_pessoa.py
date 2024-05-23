class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.__ano_nascimento = ano_nascimento

    @property
    def idade(self):
        ano_atual = 2024
        return ano_atual - self.__ano_nascimento


pessoa = Pessoa("Fábio", 2002)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
