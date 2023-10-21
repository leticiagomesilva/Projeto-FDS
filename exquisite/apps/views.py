from django.shortcuts import render
from .models import Question, Choice, Usuario

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
        'sobrenome': 'Belliato',
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

dias_da_semana = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']
numero_de_perguntas = [3, 5, 7, 9]


def inicio(request):
    return render(request, 'apps/inicio.html')

def ranking(request):
    return render(request, 'usuarios/ranking.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.sobrenome = request.POST.get('sobrenome')
    novo_usuario.pontos = request.POST.get('pontos')
    novo_usuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/acessar_ranking.html', usuarios)

def metas(request):
    context = {
        'title': 'Metas',
        'dias_da_semana': dias_da_semana,
        'numero_de_perguntas': numero_de_perguntas
    }
    return render(request, 'apps/metas.html', context)


def criar_perguntas(request):
    return render(request, 'apps/criar_perguntas.html', {'title': 'Crie sua Pergunta'})


def acessar_perguntas(request):
    return render(request, 'apps/acessar_perguntas.html', {'title': 'Acessar Perguntas'})

def salas(request):
    return render(request, 'apps/salas.html', {'title': 'Salas'})

def login(request):
    context = {
        'title': 'Login',
        'texts': ['E-mail'],
        'passwords': ['Senha'],                          # Mudar para pagina de esquecimento de senha
        'links': [{'title': 'Esqueceu sua senha?', 'ref': 'inicio'}, {'title': 'Criar Conta', 'ref': 'cadastro'}],
        'entrar': 'acessar_perguntas' # Mudar se necessário
    }
    return render(request, 'apps/login.html', context)

def cadastro(request):
    context = {
        'title': 'Cadastro',
        'texts': ['Informe seu E-mail'],
        'passwords': ['Informe sua Senha'],
        'links': [{'title': 'Login', 'ref': 'login'}],
        'entrar': 'inicio'
    }
    return render(request, 'apps/cadastro.html', context)

def pergunta(request):
    return render(request, 'apps/pergunta.html', {'title': 'pergunta'})

def resposta(request):
    return render(request, 'apps/resposta.html', {'title': 'resposta'})

def avaliar(request):
    return render(request, 'apps/avaliar.html', {'title': 'avaliar'})