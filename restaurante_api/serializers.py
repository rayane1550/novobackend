from rest_framework import serializers
from .models import pagamentos

class pagamentosSerializer (serializers.ModelSerializer):
    class Meta:
        model = pagamentos
        fields = '__all__'
        read_only_fields = ['id']
