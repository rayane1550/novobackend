from rest_framework import serializers
from .models import pagamentos

class pagamentosSerializer (serializers.ModelSerializer):
    class Meta:
        model = pagamentos
        fields = '__all__'
        read_only_fields = ['id']




from rest_framework import serializers
from .models import (
    Clientes, Funcionarios, Mesas, Categorias, Produtos, 
    Ingredientes, ProdutosIngredientes, Pedidos, ItensPedido, 
    Pagamentos, Fornecedores, Compras
)


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'


class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'


class MesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesas
        fields = '__all__'


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = '__all__'


class ProdutosIngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutosIngredientes
        fields = '__all__'


class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'


class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedores
        fields = '__all__'


class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = '__all__'


class ItensPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = '__all__'


class PedidosSerializer(serializers.ModelSerializer):
    itens = ItensPedidoSerializer(many=True, read_only=True, source='itenspedido_set')
    
    class Meta:
        model = Pedidos
        fields = '__all__'


class PagamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamentos
        fields = '__all__'

