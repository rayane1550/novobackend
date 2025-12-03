from django.db import models

class pagamentos(models.Model): 
    TIPO_CHOICES = [
    ('Tipo pagemntos', 'Tipo pagamento'),#Oque vai aparecer pro usuario(tipos de pagamentos liberados)
    ('Pix', 'Pix'),
    ('Cartão', 'Cartão'),
    ('Boleto', 'Boleto'),
]
    pedido_id = models.IntegerField()
    tipo_pagamento = models.CharField(max_length=100, choices=TIPO_CHOICES)#Esse é o Enum do banco de dados, um valor definido caso ninguem coloque nenhum valor ele vai autamaticamente
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField()  

    def __str__(self):
        return f"Pagamento {self.pedido_id} - {self.tipo_pagamento}" 
    
class pedidos(models.Model):
    TIPO_CHOICES = [
        ('STATUS','STATUS'),
        ('APROVADO','APROVADO'),
        ('CANCELADO', 'CANCELADO'),
    ]

    cliente_id = models.IntegerField()
    funcionario_id = models.CharField(max_lenght=100)
    mesa_id = models.CharField(max_lenth=100)
    data_hora = models.DateTimeField()
    status = models.CharField(max_lenth=100, choices=TIPO_CHOICES)
    observacoes = models.TextField()

    def __str__ (self):
        return f"pedidos {self.cliente_id} - {self.pedidos}" 


class itenspedido(models.Model):

    pedido_id = models.IntegerField()
    produto_id = models.CharField(max_lenght=100)
    quantidade = models.DecimalField(max_lenth=100)
    preco_unitorio = models.DecimalField()

    def __str__ (self):
        return f"itenspedido {self.pedido_id} - {self.itenspedido}"


class funcionarios(models.Model):

    nome = models.CharField(max_lenght=100)
    cargo = models.CharField(max_lenght=100)
    email = models.CharField(max_length=100)
    

    







# Create your models here.
