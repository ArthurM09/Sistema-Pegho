from django.db import models

# Criação dos modelos do banco de dados
class DadosPessoais(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)

class Contato(models.Model):
    dados_pessoais = models.OneToOneField(DadosPessoais, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    
class Experiencia(models.Model):
    dados_pessoais = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    entrada = models.DateField()
    saida = models.DateField(null=True, blank=True)  # null para trabalho atual.
    descricao = models.TextField()

class Formacao(models.Model):
    dados_pessoais = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    inicio = models.DateField()
    fim = models.DateField(null=True, blank=True)
