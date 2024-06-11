class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def calcular_idade(cls, ano, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18


pessoa = Pessoa.calcular_idade(1994, "Guilherme")
print(pessoa.nome, pessoa.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))

