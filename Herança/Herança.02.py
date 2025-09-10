class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

    def detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")
        print(f"Bônus: R${self.calcular_bonus():.2f}")


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20

funcionario1 = Funcionario("João", 2000)
gerente1 = Gerente("Maria", 5000)

print("Funcionário:")
funcionario1.detalhes()

print("\nGerente:")
gerente1.detalhes()
