from sabor_super_logico.restaurante_api import admin
from sabor_super_logico.restaurante_api import Relacionamento
from .views import listar_pagamento
from  django.urls import path, include

urlpatternes = [
    path('admin/', admin.site.urls),
    path('', include('api_sistema.urls')),
    path('pagamentos/', listar_pagamentos, name='listar_pagamentos')
]