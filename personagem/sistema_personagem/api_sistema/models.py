from django.db import models

class personagem(models.Model):
    TIPO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino')
]
    nome = models.CharField(max_length=100)
    filme = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    altura = models.FloatField()

class obra(models.Model):
    TIPO_CHOICES = [
    ('A', 'Anime'),
    ('M', 'Mangá'),
    ('L', 'Livro'),
    ('F', 'Filme'),
    ('S', 'Série')
    ]

    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    ano_lancamento = models.DateField()
    estudio_produtora = models.CharField(max_length=100)

class habilidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()


class personagem_habilidade(models.Model):
    personagem = models.ForeignKey(personagem, on_delete=models.CASCADE)
    habilidade = models.ForeignKey(habilidade, on_delete=models.CASCADE)

class ator_dublador(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)
# Create your models here.

class Relacionamento(models.Model):
    CHOICES_TIPO = [
        ('Amigo', 'Amigo'),
        ('Inimigo', 'Inimigo'),
        ('Parente', 'Parente'),
        ('Colega', 'Colega'),
    ]
    id_ralacionamento = models.AutoField(primary_key=True)
    id_personagem_origem = models.ForeignKey(personagem, on_delete=models.CASCADE, related_name='personagem_origem')
    id_personagem_destino = models.ForeignKey(personagem, on_delete=models.CASCADE, related_name='personagem_destino')
    tipo_relacionamento = models.CharField(max_length=100)