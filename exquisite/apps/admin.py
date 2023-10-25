from django.contrib import admin
from .models import Question, Choice, AvaliacaoPergunta, PerguntasBD

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(AvaliacaoPergunta)
admin.site.register(PerguntasBD)