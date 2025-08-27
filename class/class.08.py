class carro:
    def __init__(self, marca, cor, ano):
        self.marca = marca
        self.cor = cor
        self.ano = ano

    def detalhes(self):
        print(f"marca: {self.marca}, cor: {self.cor}, ano: {self.ano}")
meu_carro2 = carro("chevrolet", "azul", 2018)
meu_carro2.detalhes()

registros_pessoa2 = pessoa("joão", 35, "manutenção")
registros_pessoa3 = pessoa("maria", 29, "recursos humanos")

registros_pessoa2.apresentar()
registros_pessoa3.apresentar()

class manual:
    def __init__(self, titulo, autor, ano_publicação):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicação = ano_publicação

    def informações(self):
        print(f"titulo: {self.titulo}, autor: {self.autor}, ano_publicação: {self.ano_publicação}")

manual_2 = manual("manutenção de máquinas", "engenheiro Carlos", 2015)
manual_2.informacoes()

class produto:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

    def mostra_estoque(self):
        print(f"nome: {self.nome}, preço: {self.preço}, quantidade: {self.quantidade}")
produto2 = produto("óleo lubrificante", "R$50.00", 20)
produto3 = produto("chave inglesa", "R$30.00", 15)

produto2.mostra_estoque()
produto3.mostra_estoque()

treinamento2 = treinamento("segurança no trabalho", "técnico João", 180)
treinamento2.descrição()

class aprovado:
    def __init__(self, nome_aluno, curso, nota_final):
        self.nome_aluno = nome_aluno
        self.curso = curso
        self.nota_final = nota_final
    def resultado(self):
        print(f"nome_aluno: {self.nome_aluno}, curso: {self.curso}, nota_final: {self.nota_final}")

aluno2 = aprovado("joão", "Mecânica", 8.0)
aluno3 = aprovado("maria", "Segurança do Trabalho", 6.5)

aluno2.resultado()
aluno3.resultado()