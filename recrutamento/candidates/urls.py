from django.urls import path
from . import views

urlpatterns = [
    path('candidates/', views.candidates_list, name='candidates_list'),  # Lista todos os candidatos
    path('candidates/create/', views.create_candidate, name='create_candidate'),  # Criação de novo candidato
    path('candidates/<int:pk>/', views.candidate_detail, name='candidate_detail'),  # Visualização do candidato
    path('candidates/<int:pk>/edit/', views.update_candidate, name='update_candidate'),  # Edição do candidato
    path('candidates/<int:pk>/delete/', views.CandidateDeleteView.as_view(), name='delete_candidate'),  # Exclusão do candidato
]
