from django.db import models

# Create your models here.

class Obra(models.Model):
    TIPO_CHOICES = [
        ('Anime', 'ANIME'),
        ('Filme', 'FILME'),
        ('Serie', 'SERIE'),
        ('Livro', 'LIVRO'),
    ]

    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=5, choices=TIPO_CHOICES)
    ano_lancamento = models.IntegerField(null=True, blank=True)
    estudio_produtora = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    
class AtorDublador(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.charfield(max_length=50)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Personagem(models.Model):

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('H', 'Homi'),
        ('O', 'Outro'),
    ]
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(null=True, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    especie = models.CharField()
    desricao = models.TextField()
    ator_dublador = models.ForeignKey(AtorDublador, on_delete=models.SET_NULL, null=True)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='personagens')

    def __str__(self):
        return self.nome

