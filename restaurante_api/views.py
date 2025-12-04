from django.shortcuts import render #importando a tabela pagamentos
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import pagamentos
from .serializers import pagamentosSerializer

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def lista_pagamentos(request):
    if request.method == 'GET':
        pagamentos= pagamentos.objects.all()
        serializer = pagamentosSerializer(pagamentos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        try:
            pagamento = pagamentos.objects.get(id=request.data['id'])
            serializer = pagamentosSerializer(pagamento, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except pagamentos.DoesNotExist:
            return Response({"detail": "Pagamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'PATCH':
        try:
            pagamento = pagamentos.objects.get(id=request.data['id'])
            serializer = pagamentosSerializer(pagamento, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except pagamentos.DoesNotExist:
            return Response({"detail": "Pagamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        try:
            pagamento = pagamentos.objects.get(id=request.data['id'])
            pagamento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except pagamentos.Doe











from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Clientes, Funcionarios, Mesas, Categorias, Produtos,
    Ingredientes, ProdutosIngredientes, Pedidos, ItensPedido,
    Pagamentos, Fornecedores, Compras
)
from .serializers import (
    ClientesSerializer, FuncionariosSerializer, MesasSerializer,
    CategoriasSerializer, ProdutosSerializer, IngredientesSerializer,
    ProdutosIngredientesSerializer, PedidosSerializer, ItensPedidoSerializer,
    PagamentosSerializer, FornecedoresSerializer, ComprasSerializer
)


# ==================== CLIENTES ====================
@api_view(['GET', 'POST'])
def lista_clientes(request):
    if request.method == 'GET':
        clientes = Clientes.objects.all()
        serializer = ClientesSerializer(clientes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_cliente(request, pk):
    try:
        cliente = Clientes.objects.get(pk=pk)
    except Clientes.DoesNotExist:
        return Response({"detail": "Cliente não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ClientesSerializer(cliente)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ClientesSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==================== FUNCIONARIOS ====================
@api_view(['GET', 'POST'])
def lista_funcionarios(request):
    if request.method == 'GET':
        funcionarios = Funcionarios.objects.all()
        serializer = FuncionariosSerializer(funcionarios, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FuncionariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_funcionario(request, pk):
    try:
        funcionario = Funcionarios.objects.get(pk=pk)
    except Funcionarios.DoesNotExist:
        return Response({"detail": "Funcionário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FuncionariosSerializer(funcionario)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FuncionariosSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==================== MESAS ====================
@api_view(['GET', 'POST'])
def lista_mesas(request):
    if request.method == 'GET':
        mesas = Mesas.objects.all()
        serializer = MesasSerializer(mesas, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MesasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_mesa(request, pk):
    try:
        mesa = Mesas.objects.get(pk=pk)
    except Mesas.DoesNotExist:
        return Response({"detail": "Mesa não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MesasSerializer(mesa)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MesasSerializer(mesa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        mesa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==================== CATEGORIAS ====================
@api_view(['GET', 'POST'])
def lista_categorias(request):
    if request.method == 'GET':
        categorias = Categorias.objects.all()
        serializer = CategoriasSerializer(categorias, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CategoriasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_categoria(request, pk):
    try:
        categoria = Categorias.objects.get(pk=pk)
    except Categorias.DoesNotExist:
        return Response({"detail": "Categoria não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategoriasSerializer(categoria)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CategoriasSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==================== PRODUTOS ====================
@api_view(['GET', 'POST'])
def lista_produtos(request):
    if request.method == 'GET':
        produtos = Produtos.objects.all()
        serializer = ProdutosSerializer(produtos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProdutosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_produto(request, pk):
    try:
        produto = Produtos.objects.get(pk=pk)
    except Produtos.DoesNotExist:
        return Response({"detail": "Produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProdutosSerializer(produto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProdutosSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==================== INGREDIENTES ====================
@api_view(['GET', 'POST'])
def lista_ingredientes(request):
    if request.method == 'GET':
        ingredientes = Ingredientes.objects.all()
        serializer = IngredientesSerializer(ingredientes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = IngredientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_ingrediente(request, pk):
    try:
        ingrediente = Ingredientes.objects.get(pk=pk)
    except Ingredientes.DoesNotExist:
        return Response({"detail": "Ingrediente não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = IngredientesSerializer(ingrediente)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = IngredientesSerializer(ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==================== PEDIDOS ====================
@api_view(['GET', 'POST'])
def lista_pedidos(request):
    if request.method == 'GET':
        pedidos = Pedidos.objects.all()
        serializer = PedidosSerializer(pedidos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PedidosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_pedido(request, pk):
    try:
        pedido = Pedidos.objects.get(pk=pk)
    except Pedidos.DoesNotExist:
        return Response({"detail": "Pedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PedidosSerializer(pedido)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PedidosSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==================== ITENS DE PEDIDO ====================
@api_view(['GET', 'POST'])
def lista_itenspedido(request):
    if request.method == 'GET':
        itens = ItensPedido.objects.all()
        serializer = ItensPedidoSerializer(itens, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ItensPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_itempedido(request, pk):
    try:
        item = ItensPedido.objects.get(pk=pk)
    except ItensPedido.DoesNotExist:
        return Response({"detail": "Item de pedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItensPedidoSerializer(item)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ItensPedidoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==================== PAGAMENTOS ====================
@api_view(['GET', 'POST'])
def lista_pagamentos(request):
    if request.method == 'GET':
        pagamentos = Pagamentos.objects.all()
        serializer = PagamentosSerializer(pagamentos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PagamentosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_pagamento(request, pk):
    try:
        pagamento = Pagamentos.objects.get(pk=pk)
    except Pagamentos.DoesNotExist:
        return Response({"detail": "Pagamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PagamentosSerializer(pagamento)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PagamentosSerializer(pagamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pagamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==================== FORNECEDORES ====================
@api_view(['GET', 'POST'])
def lista_fornecedores(request):
    if request.method == 'GET':
        fornecedores = Fornecedores.objects.all()
        serializer = FornecedoresSerializer(fornecedores, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FornecedoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_fornecedor(request, pk):
    try:
        fornecedor = Fornecedores.objects.get(pk=pk)
    except Fornecedores.DoesNotExist:
        return Response({"detail": "Fornecedor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FornecedoresSerializer(fornecedor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FornecedoresSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        fornecedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==================== COMPRAS ====================
@api_view(['GET', 'POST'])
def lista_compras(request):
    if request.method == 'GET':
        compras = Compras.objects.all()
        serializer = ComprasSerializer(compras, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ComprasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalhe_compra(request, pk):
    try:
        compra = Compras.objects.get(pk=pk)
    except Compras.DoesNotExist:
        return Response({"detail": "Compra não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ComprasSerializer(compra)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ComprasSerializer(compra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        compra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
