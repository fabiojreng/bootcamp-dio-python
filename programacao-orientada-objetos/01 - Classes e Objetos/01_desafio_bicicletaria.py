class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Buzinando...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Correndo...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def to_dict(self):
        return {
            "Cor": self.cor,
            "Modelo": self.modelo,
            "Ano": self.ano,
            "Valor": self.valor,
        }


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.to_dict())

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2.to_dict())
b2.correr()
