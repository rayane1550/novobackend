from django.db import models 
#precisa importar 'models' para usar o sistema de banco de dados do django
class Mesa(models.Model):
    STATUS_CHOICES = [
        ('livre', 'livre'),
        ('ocupada', 'ocupada'),
        ('reservada', 'reservada'),
    ]
    numero = models.IntegerField() #número da mesa
    capacidade = models.IntegerField() #quantidade de pessoas que conseguem sentar na mesa
    status = models.CharField(max_length=100, choices=STATUS_CHOICES) 
#choices criar as opções que a mesa pode ter (livre, ocupada, reservada)
    def __str__(self):
        return f'Mesa {self.numero}'
#Def serve para mostrar o nome da mesa no admin

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    senha = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.nome} ({self.cargo})'

class Pedido(models.Model):
    STATUS_CHOICES = [ 
        ('status', 'Status'),
        ('aprovado', 'Aprovado'),
        ('cancelado', 'Cancelado'),
    ]

    cliente_id = models.IntegerField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    observacoes = models.TextField()

    def __str__ (self):
        return f"Pedido {self.id} - Cliente {self.cliente_id}" 

class Pagamento(models.Model): 
    TIPO_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('pix', 'Pix'),
        ('cartao', 'Cartão'),
        ('boleto', 'Boleto'),
    ]
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    tipo_pagamento = models.CharField(max_length=100, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"Pagamento {self.id} - Pedido {self.pedido.id} - {self.tipo_pagamento}" 
    
class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    TIPO_CHOICES = [
        ('vip', 'VIP'), 
        ('regular', 'Regular'), 
        ('fidelidade', 'Fidelidade'), 
    ]
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    tipo_cliente = models.CharField(max_length=50, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Compra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateTimeField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Compra {self.id} - {self.ingrediente.nome}'
    
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nome
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__ (self):
        return f"ItemPedido {self.id} - Pedido {self.pedido.id}"