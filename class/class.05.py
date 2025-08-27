class produto:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

    def mostra_estoque(self):
        print(f"ome: {self.nome}, preço: {self.preço}, quantidade: {self.quantidade}")

mostrar_produto = produto("creme para as mão", "R$100.00", 50)
mostrar_produto.mostra_estoque()