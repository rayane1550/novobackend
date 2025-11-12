from .models import Obra, AtorDublador, Personagem
from rest_framework import serializers

class AtorDubladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtorDublador
        fields = '__all__'
        read-only_fields = ['id']
    
class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'
        read-only_fields = ['id']

class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = '__all__'
        read-only_fields = ['id']