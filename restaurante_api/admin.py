from django.contrib import admin #precia importa o sistema de administração do django
from .models import ( 
    Mesa, Funcionario, Pedido, Pagamento, Ingrediente,
    Cliente, Categoria, Fornecedor, Compra, Produto, ItemPedido #Importa os modelos criados do models
)

admin.site.register(Mesa) #eles registram os modelos no sistema de administração do django, para aparecer para o usuario
admin.site.register(Funcionario)
admin.site.register(Pedido)
admin.site.register(Pagamento)
admin.site.register(Ingrediente)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Compra)
admin.site.register(Produto)
admin.site.register(ItemPedido)