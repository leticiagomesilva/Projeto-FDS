from django import forms

class ExcluirPerguntaForm(forms.Form):
    titulo = forms.CharField(max_length=255, required=True)