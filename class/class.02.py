class carro:
    def __init__(self, marca, cor, ano):
        self.marca = marca
        self.cor = cor
        self.ano = ano 

    def detalhes(self):
        print(f"marca: {self.marca}, cor: {self.cor}, ano: {self.ano}")

meu_carro1 = carro("ford", "vermelho", 2020)
meu_carro1.detalhes()
