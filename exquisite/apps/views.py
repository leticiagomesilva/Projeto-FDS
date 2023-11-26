from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def inicio(request):
    return render(request, 'apps/inicio.html')


def atualizar_ranking(request):
    return render(request, 'apps/atualizar_ranking.html')


def acessar_ranking(request):
    if request.method == 'POST':
        novo_usuario = Ranking()
        novo_usuario.posicao = request.POST.get('posicao')
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.sobrenome = request.POST.get('sobrenome')
        novo_usuario.pontos = request.POST.get('pontos')

        if novo_usuario.posicao and novo_usuario.nome and novo_usuario.sobrenome and novo_usuario.pontos:
            novo_usuario.save()

    usuarios = {
        'usuarios': Ranking.objects.all()
    }
    return render(request, 'apps/acessar_ranking.html', usuarios)


def atualizar_meta(request):
    return render(request, 'apps/atualizar_meta.html')


def acessar_meta(request):
    if request.method == 'POST':
        meta = request.POST.get('meta')
        if meta:
            metas_semana = Meta(meta=meta)
            metas_semana.save()
    
    meta = {
        'meta': Meta.objects.last()
    }

    return render(request, 'apps/acessar_meta.html', meta)


def criar_perguntas(request):
    return render(request, 'apps/criar_perguntas.html')


def acessar_perguntas(request):
    if request.method == 'POST':
        novo_pergunta = PerguntasBD()
        novo_pergunta.materia = request.POST.get('materia')
        novo_pergunta.titulo = request.POST.get('titulo')
        novo_pergunta.pergunta = request.POST.get('pergunta')
        novo_pergunta.resposta = request.POST.get('resposta')

        if novo_pergunta.materia and novo_pergunta.titulo and novo_pergunta.pergunta and novo_pergunta.resposta:
            novo_pergunta.save()

    perguntas = {
        'perguntas': PerguntasBD.objects.all()
    }
    return render(request, 'apps/acessar_perguntas.html', perguntas)


def salas(request):
    return render(request, 'apps/salas.html')

def login(request):
    context = {
        'texts': ['E-mail'],
        'passwords': ['Senha'],                          # Mudar para pagina de esquecimento de senha
        'links': [{'title': 'Esqueceu sua senha?', 'ref': 'inicio'}, {'title': 'Criar Conta', 'ref': 'cadastro'}],
        'entrar': 'listagem_perguntas' # Mudar se necessário
    }
    return render(request, 'apps/login.html', context)


def cadastro(request):
    context = {
        'texts': ['Informe seu E-mail'],
        'passwords': ['Informe sua Senha'],
        'links': [{'title': 'Login', 'ref': 'login'}],
        'entrar': 'inicio'
    }
    return render(request, 'apps/cadastro.html', context)


def avaliar(request):
    if request.method == 'POST':
        avaliacao = request.POST.get('avaliacao')
        if avaliacao:
            avaliacao_pergunta = AvaliacaoPergunta(avaliacao=avaliacao)
            avaliacao_pergunta.save()
            return redirect('avaliacao_sucesso')

    return render(request, 'apps/avaliar.html')


def avaliacao_sucesso(request):
    return render(request, 'apps/avaliacao_sucesso.html')

def responder(request, pergunta_id):
    pergunta = get_object_or_404(PerguntasBD, id_pergunta=pergunta_id)
    frase_pergunta = pergunta.pergunta
    erro = False

    if request.method == 'GET':
        nova_resposta = request.GET.get('resposta', '')

        if pergunta.resposta == nova_resposta:
            return redirect('resposta_correta')
        else:
            erro = True
        
    
    return render(request, 'apps/responder.html', {'title': 'responder', 'pergunta': pergunta, 'erro': erro, 'frase_pergunta': frase_pergunta})

def resposta_correta(request):
    return render(request, 'apps/resposta_correta.html', {'title': 'resposta_correta'})

def criar_salas(request):
    return render(request, 'apps/criar_salas.html')

def acessar_salas(request):
    filtrar = False
    if request.method == 'POST':

        novo_sala = Salas()
        novo_sala.titulo_sala = request.POST.get('titulo_sala')
        novo_sala.preferencia = request.POST.get('preferencia')

        if novo_sala.titulo_sala and novo_sala.preferencia:
            novo_sala.save()

        preferencia = Filtro()
        preferencia.filtro_materia = request.POST.get('filtro_materia')

        if preferencia.filtro_materia:
            preferencia.save() 
            filtrar = True

    salas = {
        'salas': Salas.objects.all(),
        'filtro': Filtro.objects.last(),
    }
    return render(request, 'apps/acessar_salas.html', {**salas, 'bool': filtrar})

def filtrar_salas(request):
    return render(request, 'apps/filtrar_salas.html')

def excluir_pergunta(request):
    erro = False
    if request.method == 'POST':
        form = ExcluirPerguntaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            try:
                pergunta = get_object_or_404(PerguntasBD, titulo=titulo)
                pergunta.delete()
                return redirect('listagem_perguntas')
            except:
                erro = True
                return render(request, 'apps/excluir_pergunta.html', {'form': form, "erro": erro})
        else:
            return redirect('excluir_pergunta')
    else:
        form = ExcluirPerguntaForm()

    return render(request, 'apps/excluir_pergunta.html', {'form': form})