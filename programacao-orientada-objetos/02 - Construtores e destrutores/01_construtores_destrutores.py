class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("Falando")

    def dormir(self):
        self.acordado = False
        print("Dormindo")


c = Cachorro("Chappie", "amarelo")
c.falar()
c.dormir()
del c
c.dormir()
