from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

def pesquisar(request):

    resultado = Produto.objects.filter(nome = 'manga')
    print(resultado)
    print("Pesquisando...")
    return HttpResponse(resultado)









# Create your views here.