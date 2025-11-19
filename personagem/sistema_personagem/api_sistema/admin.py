from django.contrib import admin
from .models import personagem, obra, habilidade, personagem_habilidade, ator_dublador, Relacionamento


admin.site.register(personagem)
# Register your models here.
 
admin.site.register(obra)
admin.site.register(habilidade)
admin.site.register(personagem_habilidade)
admin.site.register(ator_dublador)
admin.site.register(Relacionamento)
