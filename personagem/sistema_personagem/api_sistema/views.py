from django.shortcuts import render
from rest_framework.response import Response
from .models import personagem, obra, habilidade, personagem_habilidade, ator_dublador, Relacionamento_detalhe
from .serializers import PersonagemSerializer, ObraSerializer, HabilidadeSerializer, PersonagemHablidadeSeliazer, RelacionamentoSerializer, atorDubladorSerializer
from rest_framework.decorators import api_view
from rest_framework import status




@api_view(['GUET'])
def lista_personagens(request):
    if request.method == 'GET':
        personagens = personagem.objects.all()
        serializer = PersonagemSerializer(personagens, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def listar_obra(request, id):
    obra = obra.objects(pk=id)
    serializer = ObraSerializer(obra, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_habilidade(request, id):
    habilidade = habilidade.objects(pk=id)
    serializer = HabilidadeSerializer(habilidade, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_personagem_habilidade(request):
    personagem_habilidade = personagem_habilidade.objects(pk=id)
    serializer = PersonagemHablidadeSeliazer(personagem_habilidade, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_ator_dublador(request):
    ator_dublador = ator_dublador.objects(pk=id)
    serializer = atorDubladorSerializer(ator_dublador, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Relacionamento(request):
    Relacionamento = Relacionamento.objects(pk=id)
    serializer = RelacionamentoSerializer(Relacionamento, many=True)
    return Response(serializer.data)

# Create your views here.
