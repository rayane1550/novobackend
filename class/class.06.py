class treinamento:
    def __init__(self, titulo, instrutor, duracao_minutos):
        self.titulo = titulo
        self.instrutor = instrutor
        self.duracao_minutos = duracao_minutos

    def descrição(self):
        print(f"titulo: {self.titulo}, instrutor: {self.instrutor}, duracao_minutos: {self.duracao_minutos}")

treinamento_informacoes = treinamento("treinamento comportamental", "rayane", 240)
treinamento_informacoes.descrição()