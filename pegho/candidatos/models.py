from django.db import models
from django.core.validators import validate_email

# Criação das classes do banco de dados
class DadosPessoais(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

class Contato(models.Model):
    email = models.EmailField(validators=[validate_email])
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    candidato = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)

class ExperienciaProfissional(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    inicio = models.DateField()
    fim = models.DateField(null=True, blank=True)
    descricao = models.TextField()
    candidato = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)

class FormacaoAcademica(models.Model):
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    inicio = models.DateField()
    fim = models.DateField(null=True, blank=True)
    candidato = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)
