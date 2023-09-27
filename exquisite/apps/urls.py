from django.urls import path

from . import views

urlpatterns = [
    path('inicio/', views.index, name="index"),
    path('salas/', views.salas, name="salas"),
    path('metas/', views.metas, name="metas"),
]