from django import forms
from .models import DadosPessoais, Contato, ExperienciaProfissional, FormacaoAcademica

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = DadosPessoais
        fields = ['nome', 'data_nascimento']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['email', 'telefone', 'endereco']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@exemplo.com'):
            raise forms.ValidationError("Email inválido")
        return email
