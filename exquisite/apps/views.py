from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("apps/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#def index(request):
#    return HttpResponse("Página de Inicio contendo as perguntas")

def salas(request):
    return HttpResponse("Página para criação/acesso das salas")

def metas(request):
    return HttpResponse("Página para adicionar metas")

