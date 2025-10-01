from django.db import models

# Create your models here.
class livro(models.Model):
    categoria = models.CharField(max_length=100)
    titulo = models.CharField(max_length=10)
    isbn = models.CharField(max_length=20)

    def _str_(self):
        return f"{self.titulo} - {self.categoria} - {self.isbn}"

class categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.nome_categoria}"
      
class livro_categoria(models.Model):
    livro = models.ForeignKey(livro, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    
    def _str_(self):
        return f"{self.livro} - {self.categoria}"


class emprestimo(models.Model):
    usuario = models.CharField(max_length=20)
    livro = models.CharField(max_length=50)
    data = models.DateField()
    devolucao = models.DateField()

    def _str_(self):
        return f"{self.usuario} - {self.livro} - {self.data} - {self.devolucao}"

class usuario(models.Model):
    nome = models.CharField(max_length=50)
    numero_identificacao = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.nome} - {self.numero_identificacao} - {self.email}"
    
class autor(models.Model):
    nome = models.CharField(max_length=50)
    biografia = models.CharField(max_length=255)

    def _str_(self):
        return f"{self.nome} - {self.biografia}"
    
    
class usuario_autor(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    

