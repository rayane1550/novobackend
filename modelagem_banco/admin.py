from django.contrib import admin
from .models import livro, emprestimo, usuario, autor, categoria, livro_categoria, usuario_autor
# Register your models here.
admin.site.register(livro)
admin.site.register(livro_categoria)
admin.site.register(emprestimo)
admin.site.register(usuario)
admin.site.register(usuario_autor)
admin.site.register(autor)
admin.site.register(categoria)


