from sistema_personagem.api_sistema import admin
from sistema_personagem.api_sistema.models import Relacionamento
from .views import listar_personagens, criar_personagem, listar_obra, listar_habilidade, listar_personagem_habilidade, listar_ator_dublador, listar_Relacionamento_detalhe
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_sistema.urls')),
    path('personagens/', listar_personagens, name='listar_personagens'),
    path('obras/', listar_obra, name='listar_obra'),
    path('habilidade/', listar_habilidade, name='listar_habilidades'),
    path('personagem_habilidades/', listar_personagem_habilidade, name='listar_personagem_habilidade'),
    path('ator_dublador/', listar_ator_dublador, name='listar_ator_dublador'),
    path('Relacionamento/', Relacionamento, name='Relacionamento'),
]