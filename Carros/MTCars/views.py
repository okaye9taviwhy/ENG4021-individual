from django.shortcuts import render
from MTCars.models import MTCars

# Create your views here.

def home(request):
    '''
    Renderiza a home-page.
    Como a home-page é uma pagina estática, 
    não precisa de variáveis de contexto.
    '''
    return render(request, 'home.html')