from django.urls import path #importar a função path para definir as rotas da API
from .views import criar_listar_cliente, detalhe_cliente, criar_listar_funcionarios, detalhe_funcionario, criar_listar_pagamentos, detalhe_pagamento, criar_listar_categorias, detalhe_categoria, criar_listar_produto, detalhe_produto, criar_listar_ingredientes, detalhe_ingrediente, criar_listar_ingredientes, detalhe_itempedido, criar_listar_itempedido, detalhe_itempedido, criar_listar_pagamentos, detalhe_pagamento, criar_listar_fornecedores, detalhe_fornecedor, criar_listar_compras, detalhe_compra, criar_listar_mesas, detalhe_mesa, criar_listar_pedidos, detalhe_pedido
#importar todas as views criadas para cada modelo
urlpatterns = [

    path('clientes/', criar_listar_cliente, name='lista_cliente'),#definir a rota para listar e criar clientes
    path('clientes/<int:pk>/', detalhe_cliente, name='detalhe_cliente'),#definir a rota para detalhar, atualizar e deletar um cliente específico pelo seu ID
    
    path('funcionarios/', criar_listar_funcionarios, name='lista_funcionarios'),
    path('funcionarios/<int:pk>/', detalhe_funcionario, name='detalhe_funcionario'),
    
    path('mesas/', criar_listar_mesas, name='lista_mesas'),
    path('mesas/<int:pk>/', detalhe_mesa, name='detalhe_mesa'),

    path('categorias/', criar_listar_categorias, name='lista_categorias'),
    path('categorias/<int:pk>/', detalhe_categoria, name='detalhe_categoria'),
    
    path('produtos/', criar_listar_produto, name='lista_produtos'),
    path('produtos/<int:pk>/', detalhe_produto, name='detalhe_produto'),
 
    path('ingredientes/', criar_listar_ingredientes, name='lista_ingredientes'),
    path('ingredientes/<int:pk>/', detalhe_ingrediente, name='detalhe_ingrediente'),
  
    path('pedidos/', criar_listar_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pk>/', detalhe_pedido, name='detalhe_pedido'),

    path('itempedido/', criar_listar_itempedido, name='lista_itempedido'),
    path('itempedido/<int:pk>/', detalhe_itempedido, name='detalhe_itempedido'),

    path('pagamentos/', criar_listar_pagamentos, name='listar_criar_pagamentos'),
    path('pagamentos/<int:id>/', detalhe_pagamento, name='detalhe_pagamento'),

    path('fornecedores/', criar_listar_fornecedores, name='lista_fornecedores'),
    path('fornecedores/<int:pk>/', detalhe_fornecedor, name='detalhe_fornecedor'),

    path('compras/', criar_listar_compras, name='lista_compras'),
    path('compras/<int:pk>/', detalhe_compra, name='detalhe_compra'),
]

