from django.shortcuts import render
from .models import Question, Choice

pessoas = [
    {
        'nome': 'Ricardo',
        'sobrenome': 'Costa',
        'pontuacao': '586',
        'posicao': '1', 
    },
    {
        'nome': 'Letícia',
        'sobrenome': 'Gomes',
        'pontuacao': '431',
        'posicao': '2',
    },
    {
        'nome': 'Hugo',
        'sobrenome': 'Rocha',
        'pontuacao': '312',
        'posicao': '3',
    },
    {
        'nome': 'Letícia',
        'sobrenome': 'Lopes',
        'pontuacao': '279',
        'posicao': '4',
    },
    {
        'nome': 'Gabriel',
        'sobrenome': 'Beliatto',
        'pontuacao': '195',
        'posicao': '5',
    },
    {
        'nome': 'Gabriel',
        'sobrenome': 'Bezerra',
        'pontuacao': '182',
        'posicao': '6',
    },
]

def inicio(request):
    return render(request, 'apps/inicio.html')

def ranking(request):
    context = {
        'title': 'Ranking',
        'pessoas': pessoas
    }
    return render(request, 'apps/ranking.html', context)

def metas(request):
    return render(request, 'apps/metas.html', {'title': 'Metas'})

def criar_perguntas(request):
    return render(request, 'apps/criar_perguntas.html', {'title': 'Crie sua Pergunta'})

def acessar_perguntas(request):
    return render(request, 'apps/acessar_perguntas.html', {'title': 'Acessar Perguntas'})

def perfil(request):
    return render(request, 'apps/perfil.html', {'title': 'Perfil'})

def salas(request):
    return render(request, 'apps/salas.html', {'title': 'Salas'})