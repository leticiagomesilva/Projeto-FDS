from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('ranking/', views.ranking, name="ranking"),
    path('acessar_ranking/', views.usuarios, name="listagem_ranking"),
    path('atualizar_meta/', views.atualizar_meta, name="atualizar_meta"),
    path('acessar_meta/', views.acessar_meta, name="acessar_meta"),
    path('criar_perguntas/', views.criar_perguntas, name="criar_perguntas"),
    path('acessar_perguntas/', views.acessar_perguntas, name="listagem_perguntas"),
    path('login/', views.login, name="login"),
    path('salas/', views.salas, name="salas"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('avaliar/', views.avaliar, name="avaliar"),
    path('avaliacao_sucesso/', views.avaliacao_sucesso, name='avaliacao_sucesso'),
]