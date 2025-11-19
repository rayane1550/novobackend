from rest_framework import serializers
from .models import personagem, obra, habilidade, personagem_habilidade, ator_dublador, Relacionamento

class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = personagem
        fields = '__all__'
        read_only_fields = ['id']

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = obra
        fields = '__all__'
        read_only_fields = ['id']

class HabilidadeSerializer(serializers.ModelSerializer):
    class meta:
        model = habilidade 
        fields = '__all_'
        read_only_fields = ['id']

class PersonagemHablidadeSeliazer(serializers.ModelSerializer):
    class Meta:
        model = personagem_habilidade
        fields = '__all__'
        read_only_fields = ['id']

class atorDubladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ator_dublador
        fields = '__all__'
        read_only_fields = ['id']

class RelacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacionamento
        fields = '__all__'
        read_only_fields = ['id']