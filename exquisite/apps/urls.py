from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('atualizar_ranking/', views.atualizar_ranking, name="atualizar_ranking"),
    path('acessar_ranking/', views.acessar_ranking, name="listagem_ranking"),
    path('atualizar_meta/', views.atualizar_meta, name="atualizar_meta"),
    path('acessar_meta/', views.acessar_meta, name="acessar_meta"),
    path('criar_perguntas/', views.criar_perguntas, name="criar_perguntas"),
    path('acessar_perguntas/', views.acessar_perguntas, name="listagem_perguntas"),
    path('login/', views.login, name="login"),
    path('salas/', views.salas, name="salas"),
    path('criar_salas/', views.criar_salas, name="criar_salas"),
    path('acessar_salas/', views.acessar_salas, name="acessar_salas"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('avaliar/', views.avaliar, name="avaliar"),
    path('avaliacao_sucesso/', views.avaliacao_sucesso, name='avaliacao_sucesso'),
    path('acessar_perguntas/responder/<int:pergunta_id>/', views.responder, name='responder'),
    path('acessar_perguntas/responder/resposta_correta/', views.resposta_correta, name='resposta_correta'),
]