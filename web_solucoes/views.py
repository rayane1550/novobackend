from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá, bem-vindo ao Sistema de Soluções!")
def home(request):
    return render(request, 'solucoes_web.html')
def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

# Create your views here.