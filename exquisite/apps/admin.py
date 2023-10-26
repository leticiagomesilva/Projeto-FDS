from django.contrib import admin
from .models import *

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(AvaliacaoPergunta)
admin.site.register(PerguntasBD)
admin.site.register(Meta)
admin.site.register(Ranking)