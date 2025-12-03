from django.shortcuts import render #importando a tabela pagamentos
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import pagamentos
from .serializers import pagamentosSerializer

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def lista_pagamentos(request):
    if request.method == 'GET':
        pagamentos= pagamentos.objects.all()
        serializer = pagamentosSerializer(pagamentos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        try:
            pagamento = pagamentos.objects.get(id=request.data['id'])
            serializer = pagamentosSerializer(pagamento, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except pagamentos.DoesNotExist:
            return Response({"detail": "Pagamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'PATCH':
        try:
            pagamento = pagamentos.objects.get(id=request.data['id'])
            serializer = pagamentosSerializer(pagamento, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except pagamentos.DoesNotExist:
            return Response({"detail": "Pagamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        try:
            pagamento = pagamentos.objects.get(id=request.data['id'])
            pagamento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except pagamentos.Doe


# Create your views here.
