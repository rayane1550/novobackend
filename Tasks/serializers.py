from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , serializers
from .models import task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ('id', 'titulo', 'descricao', 'Criado_em', 'completado')

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = tasks.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Mensagem": "Tarefa criada com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
