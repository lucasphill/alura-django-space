from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    
    dados = {
        1: {'nome': 'Nebulosa de Carina',
            'legenda': 'wbbbtelescope.org / Nasa / James Webb'},
        2: {'nome': 'Galaxia NGC 1079',
            'legenda': 'nasa.org / Nasa / Hubble'}
    }

    return render(request, 'galeria/index.html', {'cards':dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')