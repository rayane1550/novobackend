from django.shortcuts import render

def pizza_do_dia(request):
    """
    Essa view renderiza o template para a página “Pizza do Dia”.
    """
    return render(request, 'pizza_do_dia.html')

def promocoes(request):
    """
    Essa view renderiza o template para a página “Promoções”.
    """
    return render(request, 'promocoes.html')
