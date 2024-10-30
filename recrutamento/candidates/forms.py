from django import forms
from .models import DadosPessoais, Contato, Experiencia, Formacao

class DadosPessoaisForm(forms.ModelForm):
    class Meta:
        model = DadosPessoais
        fields = '__all__'  # Inclui todos os campos do modelo

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = '__all__'

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'
