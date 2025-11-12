from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    Criado_em = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)





# Create your models here.
