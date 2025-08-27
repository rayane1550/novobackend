class pessoa:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor
        
    def apresentar(self):
        print(f"nome: {self.nome}, idade: {self.idade}, setor: {self.setor}")

registros_pessoa = pessoa("rayane", 17, "TI")
registros_pessoa.apresentar()