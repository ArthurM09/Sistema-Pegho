from django.contrib import admin
from .models import DadosPessoais, Contato, Experiencia, Formacao

@admin.register(DadosPessoais)
class DadosPessoaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'cpf')

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('dados_pessoais', 'email', 'telefone', 'endereco')

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('dados_pessoais', 'cargo', 'empresa', 'entrada', 'saida', 'descricao')

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('dados_pessoais', 'instituicao', 'curso', 'inicio', 'fim')
