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
    

    

    from django.db import models
from django.core.validators import MinValueValidator


class Clientes(models.Model):
    TIPO_CLIENTE_CHOICES = [
        ('VIP', 'VIP'),
        ('Regular', 'Regular'),
        ('Fidelidade', 'Fidelidade'),
    ]
    
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    tipo_cliente = models.CharField(max_length=50, choices=TIPO_CLIENTE_CHOICES)
    
    class Meta:
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nome


class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    senha = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'funcionarios'
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
    
    def __str__(self):
        return self.nome


class Mesas(models.Model):
    STATUS_CHOICES = [
        ('Livre', 'Livre'),
        ('Ocupada', 'Ocupada'),
        ('Reservada', 'Reservada'),
    ]
    
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    capacidade = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    
    class Meta:
        db_table = 'mesas'
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
    
    def __str__(self):
        return f'Mesa {self.numero}'


class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nome


class Ingredientes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unidade_medida = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'ingredientes'
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
    
    def __str__(self):
        return self.nome


class Produtos(models.Model):
    id = models.AutoField(primary_key=True)
    categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE, db_column='categoria_id')
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    estoque = models.IntegerField(validators=[MinValueValidator(0)])
    ingredientes = models.ManyToManyField(Ingredientes, through='ProdutosIngredientes', related_name='produtos')
    
    class Meta:
        db_table = 'produtos'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        return self.nome


class ProdutosIngredientes(models.Model):
    id = models.AutoField(primary_key=True)
    produto_id = models.ForeignKey(Produtos, on_delete=models.CASCADE, db_column='produto_id')
    ingrediente_id = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, db_column='ingrediente_id')
    quantidade_usada = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    class Meta:
        db_table = 'produtos_ingredientes'
        verbose_name = 'Produto Ingrediente'
        verbose_name_plural = 'Produtos Ingredientes'
        unique_together = ['produto_id', 'ingrediente_id']
    
    def __str__(self):
        return f'{self.produto_id.nome} - {self.ingrediente_id.nome}'


class Fornecedores(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'fornecedores'
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
    
    def __str__(self):
        return self.nome


class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    fornecedor_id = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, db_column='fornecedor_id')
    ingrediente_id = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, db_column='ingrediente_id')
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data_compra = models.DateTimeField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    class Meta:
        db_table = 'compras'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
    
    def __str__(self):
        return f'Compra {self.id} - {self.ingrediente_id.nome}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Atualiza o estoque do ingrediente
        self.ingrediente_id.quantidade_estoque += self.quantidade
        self.ingrediente_id.save()


class Pedidos(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Preparo', 'Em Preparo'),
        ('Pronto', 'Pronto'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
    ]
    
    id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE, db_column='cliente_id')
    funcionario_id = models.ForeignKey(Funcionarios, on_delete=models.CASCADE, db_column='funcionario_id')
    mesa_id = models.ForeignKey(Mesas, on_delete=models.CASCADE, db_column='mesa_id')
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    observacoes = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return f'Pedido {self.id} - {self.cliente_id.nome}'


class ItensPedido(models.Model):
    id = models.AutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedidos, on_delete=models.CASCADE, db_column='pedido_id')
    produto_id = models.ForeignKey(Produtos, on_delete=models.CASCADE, db_column='produto_id')
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    class Meta:
        db_table = 'itenspedido'
        verbose_name = 'Item de Pedido'
        verbose_name_plural = 'Itens de Pedido'
    
    def __str__(self):
        return f'Item {self.id} - Pedido {self.pedido_id.id}'


class Pagamentos(models.Model):
    TIPO_PAGAMENTO_CHOICES = [
        ('Dinheiro', 'Dinheiro'),
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('Cartão de Débito', 'Cartão de Débito'),
        ('PIX', 'PIX'),
    ]
    
    id = models.AutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedidos, on_delete=models.CASCADE, db_column='pedido_id')
    tipo_pagamento = models.CharField(max_length=50, choices=TIPO_PAGAMENTO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    data_hora = models.DateTimeField()
    
    class Meta:
        db_table = 'pagamentos'
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
    
    def __str__(self):
        return f'Pagamento {self.id} - Pedido {self.pedido_id.id}'









# Create your models here.
