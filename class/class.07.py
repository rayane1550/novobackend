class aprovado:
    def __init__(self, nome_aluno, curso, nota_final):
        self.nome_aluno = nome_aluno
        self.curso = curso
        self.nota_final = nota_final
    def resultado(self):
        print(f"nome_aluno: {self.nome_aluno}, curso: {self.curso}, nota_final: {self.nota_final}")

aluno1 = aprovado("rayane", "Desenvolvimento", 9.5)
aluno1.resultado()