from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('ranking/', views.ranking, name="ranking"),
    path('acessar_ranking/', views.usuarios, name="listagem_ranking"),
    path('metas/', views.metas, name="metas"),
    path('criar_perguntas/', views.criar_perguntas, name="criar_perguntas"),
    path('acessar_perguntas/', views.acessar_perguntas, name="acessar_perguntas"),
    path('login/', views.login, name="login"),
    path('salas/', views.salas, name="salas"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('pergunta', views.pergunta, name="pergunta"),
    path('resposta', views.resposta, name="resposta"),
    path('avaliar', views.avaliar, name="avaliar"),
]