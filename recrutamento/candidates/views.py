from django.shortcuts import render, redirect, get_object_or_404
from .models import DadosPessoais
from .forms import DadosPessoaisForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

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
