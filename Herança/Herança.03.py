class Voador:
    def __init__(self):
        pass #pass para não precisar colocar um metodo
    def voar(self): #metodo
        print("patinho voandooo")

class Aquatico:
    def __init__(self):
        pass
    def nadar(self):
        print("patinho nadandooo")

class Pato(Voador, Aquatico):
    def detalhes(self, nome):
        print("Detalhes do pato:")
        print(f"Nome: {nome}")
        super().nadar()

pato = Pato()
pato.voar()
pato.nadar()
pato.detalhes("Donald")
