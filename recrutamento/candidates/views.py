from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets # type: ignore
from .models import DadosPessoais, Contato, Experiencia, Formacao
from .serializers import DadosPessoaisSerializer, ContatoSerializer, ExperienciaSerializer, FormacaoSerializer
from .forms import DadosPessoaisForm, ContatoForm, ExperienciaForm, FormacaoForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

# *** MODELO DADOS PESSOAIS ***
# Criar novos dados de candidatos
def create_candidate(request):
    if request.method == "POST":
        form = DadosPessoaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidates_list')  # Redireciona para a lista após salvar
    else:
        form = DadosPessoaisForm()
    return render(request, 'candidates/create_candidate.html', {'form': form})

# Listar e exibir detalhes de cada candidato
def candidates_list(request):
    candidates = DadosPessoais.objects.all()  # Obtém todos os candidatos
    return render(request, 'candidates/candidates_list.html', {'candidates': candidates})

def candidate_detail(request, pk):
    candidate = get_object_or_404(DadosPessoais, pk=pk)  # Obtém um candidato pelo ID
    return render(request, 'candidates/candidate_detail.html', {'candidate': candidate})

# Atualizar informações de um candidato
def update_candidate(request, pk):
    candidate = get_object_or_404(DadosPessoais, pk=pk)
    if request.method == "POST":
        form = DadosPessoaisForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidates_list')  # Redireciona para a lista após a atualização
    else:
        form = DadosPessoaisForm(instance=candidate)
    return render(request, 'candidates/update_candidate.html', {'form': form, 'candidate': candidate})

# Excluir um candidato
class CandidateDeleteView(DeleteView):
    model = DadosPessoais
    template_name = 'candidates/delete_candidate.html'
    success_url = reverse_lazy('candidates_list')  # Redireciona para a lista após a exclusão


# *** MODELO CONTATO ***
# Criar contato
def create_contact(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')
    else:
        form = ContatoForm()
    return render(request, 'candidates/create_contact.html', {'form': form})

# Lista dos contatos
def contacts_list(request):
    contacts = Contato.objects.all()
    return render(request, 'candidates/contacts_list.html', {'contacts': contacts})

# Detalhes do contato
def contact_detail(request, pk):
    contact = get_object_or_404(Contato, pk=pk)
    return render(request, 'candidates/contact_detail.html', {'contact': contact})

# Atualizar Contato
def update_contact(request, pk):
    contact = get_object_or_404(Contato, pk=pk)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')
    else:
        form = ContatoForm(instance=contact)
    return render(request, 'candidates/update_contact.html', {'form': form, 'contact': contact})

# Deletar Contato
class ContactDeleteView(DeleteView):
    model = Contato
    template_name = 'candidates/delete_contact.html'
    success_url = reverse_lazy('contacts_list')


# *** MODELO EXPERIENCIA ***
# Criar Experiencia
def create_work_experience(request):
    if request.method == "POST":
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_experience_list')
    else:
        form = ExperienciaForm()
    return render(request, 'candidates/create_work_experience.html', {'form': form})

# Lista das experiencias
def work_experience_list(request):
    work_experiences = Experiencia.objects.all()
    return render(request, 'candidates/work_experience_list.html', {'work_experiences': work_experiences})

# Detalhes da Experiencia
def work_experience_detail(request, pk):
    work_experience = get_object_or_404(Experiencia, pk=pk)
    return render(request, 'candidates/work_experience_detail.html', {'work_experience': work_experience})

# Atualizar Experiencia
def update_work_experience(request, pk):
    work_experience = get_object_or_404(Experiencia, pk=pk)
    if request.method == "POST":
        form = ExperienciaForm(request.POST, instance=work_experience)
        if form.is_valid():
            form.save()
            return redirect('work_experience_list')
    else:
        form = ExperienciaForm(instance=work_experience)
    return render(request, 'candidates/update_work_experience.html', {'form': form, 'work_experience': work_experience})

# Deletar Experiencia
class WorkExperienceDeleteView(DeleteView):
    model = Experiencia
    template_name = 'candidates/delete_work_experience.html'
    success_url = reverse_lazy('work_experience_list')


# *** MODELO FORMACAO ***
# Criar Formação
def create_education(request):
    if request.method == "POST":
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('education_list')
    else:
        form = FormacaoForm()
    return render(request, 'candidates/create_education.html', {'form': form})

# Lista das Formações
def education_list(request):
    educations = Formacao.objects.all()
    return render(request, 'candidates/education_list.html', {'educations': educations})

# Detalhes da Formacao
def education_detail(request, pk):
    education = get_object_or_404(Formacao, pk=pk)
    return render(request, 'candidates/education_detail.html', {'education': education})

# Atualizar Formacao
def update_education(request, pk):
    education = get_object_or_404(Formacao, pk=pk)
    if request.method == "POST":
        form = FormacaoForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('education_list')
    else:
        form = FormacaoForm(instance=education)
    return render(request, 'candidates/update_education.html', {'form': form, 'education': education})

# Deletar Formacao
class EducationDeleteView(DeleteView):
    model = Formacao
    template_name = 'candidates/delete_education.html'
    success_url = reverse_lazy('education_list')


# Viewsets da API REST para cada modelo
class DadosPessoaisViewSet(viewsets.ModelViewSet):
    queryset = DadosPessoais.objects.all()
    serializer_class = DadosPessoaisSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

class FormacaoViewSet(viewsets.ModelViewSet):
    queryset = Formacao.objects.all()
    serializer_class = FormacaoSerializer
