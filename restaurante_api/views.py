from django.shortcuts import render #importar o render do django para renderizar que é uma função que vai processar as requisições HTTP
from rest_framework.decorators import api_view #from vai importar o decorador api_view do rest framework para definir os métodos HTTP permitidos em cada view
from rest_framework.response import Response #from vai importar a classe Response do rest framework para retornar respostas HTTP
from rest_framework import status #vai importar o status do rest framework para usar os códigos de status HTTP nas respostas
from .models import ( #importando todos os modelos criados
    Mesa, Funcionario, Pedido, Pagamento, Ingrediente,
    Cliente, Categoria, Fornecedor, Compra, Produto, ItemPedido
)
from .serializers import ( #importando todos os serializers criados
    MesaSerializer, FuncionarioSerializer, PedidoSerializer, PagamentoSerializer,
    IngredienteSerializer, ClienteSerializer, CategoriaSerializer,
    FornecedorSerializer, CompraSerializer, ProdutoSerializer, ItemPedidoSerializer
)


@api_view(['GET', 'POST']) #Vai definir os métodos HTTP permitidos (GET e POST)
def criar_listar_pagamentos(request):
    if request.method == 'GET':#O metodo que vai listar todos os pagamentos
        pagamentos = Pagamento.objects.all() #pegar todos os pagamentos do banco de dados e listar para o usuario
        serializer = PagamentoSerializer(pagamentos, many=True)#serializar os dados dos pagamentos para o formato JSON
        return Response(serializer.data) #retornar a resposta com os dados serializados

    elif request.method == 'POST':#O metodo que vai criar um novo pagamento
        serializer = PagamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)#vai dar a resposta com os dados do pagamento criado e o status 201 (criado)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#vai dar a resposta com os erros de validação e o status 400 (requisição inválida)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])# Vai definir os métodos HTTP permitidos (GET, PUT, PATCH e DELETE)
def detalhe_pagamento(request, id): 
    try:
        pagamento = Pagamento.objects.get(pk=id)
    except Pagamento.DoesNotExist: 
        return Response({"detail": "Pagamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PagamentoSerializer(pagamento)
        return Response(serializer.data)

    elif request.method == 'PUT': #Atualizar um pagamento existente
        serializer = PagamentoSerializer(pagamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':#Atualizar parcialmente um pagamento existente
        serializer = PagamentoSerializer(pagamento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Pagamento atualizado com sucesso", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': #Deletar um pagamento existente
        pagamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    

@api_view(['GET', 'POST'])
def criar_listar_cliente(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalhe_cliente(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return Response({"detail": "Cliente não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_listar_funcionarios(request):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalhe_funcionario(request, pk):
    try:
        funcionario = Funcionario.objects.get(pk=pk)
    except Funcionario.DoesNotExist:
        return Response({"detail": "Funcionário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FuncionarioSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = FuncionarioSerializer(funcionario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_listar_mesas(request):
    if request.method == 'GET':
        mesas = Mesa.objects.all()
        serializer = MesaSerializer(mesas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalhe_mesa(request, pk):
    try:
        mesa = Mesa.objects.get(pk=pk)
    except Mesa.DoesNotExist:
        return Response({"detail": "Mesa não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MesaSerializer(mesa)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MesaSerializer(mesa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = MesaSerializer(mesa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        mesa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_listar_categorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalhe_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response({"detail": "Categoria não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = CategoriaSerializer(categoria, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_listar_produto(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalhe_produto(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
    except Produto.DoesNotExist:
        return Response({"detail": "Produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = ProdutoSerializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_listar_ingredientes(request):
    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalhe_ingrediente(request, pk):
    try:
        ingrediente = Ingrediente.objects.get(pk=pk)
    except Ingrediente.DoesNotExist:
        return Response({"detail": "Ingrediente não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IngredienteSerializer(ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = IngredienteSerializer(ingrediente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_listar_pedidos(request):
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalhe_pedido(request, pk):
    try:
        pedido = Pedido.objects.get(pk=pk)
    except Pedido.DoesNotExist:
        return Response({"detail": "Pedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = PedidoSerializer(pedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_listar_itempedido(request):
    if request.method == 'GET':
        itens = ItemPedido.objects.all()
        serializer = ItemPedidoSerializer(itens, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalhe_itempedido(request, pk):
    try:
        item = ItemPedido.objects.get(pk=pk)
    except ItemPedido.DoesNotExist:
        return Response({"detail": "Item de pedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItemPedidoSerializer(item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ItemPedidoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = ItemPedidoSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def criar_listar_fornecedores(request):
    if request.method == 'GET':
        fornecedores = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedores, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalhe_fornecedor(request, pk):
    try:
        fornecedor = Fornecedor.objects.get(pk=pk)
    except Fornecedor.DoesNotExist:
        return Response({"detail": "Fornecedor não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = FornecedorSerializer(fornecedor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fornecedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def criar_listar_compras(request):
    if request.method == 'GET':
        compras = Compra.objects.all()
        serializer = CompraSerializer(compras, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalhe_compra(request, pk):
    try:
        compra = Compra.objects.get(pk=pk)
    except Compra.DoesNotExist:
        return Response({"detail": "Compra não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CompraSerializer(compra)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompraSerializer(compra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = CompraSerializer(compra, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        compra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)