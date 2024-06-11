class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_alunos(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_alunos(aluno_1, aluno_2)

Estudante.escola = "Python"  # tem acesso a variável, pois é da classe
aluno_3 = Estudante("Chappie", 3)
mostrar_alunos(aluno_1, aluno_2, aluno_3)
