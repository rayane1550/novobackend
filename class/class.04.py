class manual:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def informacoes(self):
        print(f"titulo: {self.titulo}, autor: {self.autor}, ano_publicacao: {self.ano_publicacao}")

manual_1 = manual("python", "guido van rossum", 1991)
manual_1.informacoes()