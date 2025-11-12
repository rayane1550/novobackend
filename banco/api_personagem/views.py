from rest_framework.decorators import api_view
from .models import Obra, AtorDublador, Personagem
from .serializers import ObraSerializer, AtorDubladorSerializer, PersonagemSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def obra_detalhes(request, id):
    obra = Obra.objects.get(pk=id)
    serializer = ObraSerializer(obra, many=True)
    return Response(serializer.data)

# Create your views here.
