from rest_framework import serializers #from vai importar o serializers do rest framework 
from .models import (
    Cliente, Funcionario, Mesa, Categoria, Produto, 
    Ingrediente, Pedido, ItemPedido, 
    Pagamento, Fornecedor, Compra #importando todos os modelos criados
)

class ClienteSerializer(serializers.ModelSerializer): #criar sempre as classes "ClienteSerializer" ou outras que vai herdar de serializers.ModelSerializer
    class Meta:
        model = Cliente #inclui todos os campos do modelo cliente na API
        fields = '__all__'
        read_only_fields = ['id']


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'
        

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):

    itens = ItemPedidoSerializer(many=True, read_only=True) 
    
    class Meta:
        model = Pedido
        fields = '__all__'


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'