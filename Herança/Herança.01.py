class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def detalhes(self):
        print(f"Informações do veículo: Marca - {self.marca}, Modelo - {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, quantidade_portas):
        super().__init__(marca, modelo)
        self.quantidade_portas = quantidade_portas

    def heranca(self):
        print(f"Quantidade de portas: {self.quantidade_portas}")
        print(f"Marca herdada: {self.marca}")


veiculo1 = Carro("Toyota", "Corolla", 4)

veiculo1.detalhes()
veiculo1.heranca()
