from sabor_super_logico.restaurante_api import admin
from sabor_super_logico.restaurante_api import Relacionamento
from .views import listar_pagamento
from  django.urls import path, include

urlpatternes = [
    path('admin/', admin.site.urls),
    path('', include('api_sistema.urls')),
    path('pagamentos/', listar_pagamentos, name='listar_pagamentos')
]





from django.urls import path
from . import views

urlpatterns = [
    # Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:pk>/', views.detalhe_cliente, name='detalhe_cliente'),
    
    # Funcionários
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/<int:pk>/', views.detalhe_funcionario, name='detalhe_funcionario'),
    
    # Mesas
    path('mesas/', views.lista_mesas, name='lista_mesas'),
    path('mesas/<int:pk>/', views.detalhe_mesa, name='detalhe_mesa'),
    
    # Categorias
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<int:pk>/', views.detalhe_categoria, name='detalhe_categoria'),
    
    # Produtos
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
    
    # Ingredientes
    path('ingredientes/', views.lista_ingredientes, name='lista_ingredientes'),
    path('ingredientes/<int:pk>/', views.detalhe_ingrediente, name='detalhe_ingrediente'),
    
    # Pedidos
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pk>/', views.detalhe_pedido, name='detalhe_pedido'),
    
    # Itens de Pedido
    path('itenspedido/', views.lista_itenspedido, name='lista_itenspedido'),
    path('itenspedido/<int:pk>/', views.detalhe_itempedido, name='detalhe_itempedido'),
    
    # Pagamentos
    path('pagamentos/', views.lista_pagamentos, name='lista_pagamentos'),
    path('pagamentos/<int:pk>/', views.detalhe_pagamento, name='detalhe_pagamento'),
    
    # Fornecedores
    path('fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('fornecedores/<int:pk>/', views.detalhe_fornecedor, name='detalhe_fornecedor'),
    
    # Compras
    path('compras/', views.lista_compras, name='lista_compras'),
    path('compras/<int:pk>/', views.detalhe_compra, name='detalhe_compra'),
]

