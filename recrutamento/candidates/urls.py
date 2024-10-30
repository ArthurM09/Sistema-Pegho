from django.urls import path
from . import views

urlpatterns = [
    # URLs para dados pessoais
    path('candidates/', views.candidates_list, name='candidates_list'),  # Lista todos os candidatos
    path('candidates/create/', views.create_candidate, name='create_candidate'),  # Criação de novo candidato
    path('candidates/<int:pk>/', views.candidate_detail, name='candidate_detail'),  # Visualização do candidato
    path('candidates/<int:pk>/edit/', views.update_candidate, name='update_candidate'),  # Edição do candidato
    path('candidates/<int:pk>/delete/', views.CandidateDeleteView.as_view(), name='delete_candidate'),  # Exclusão do candidato

    # URLs para contato
    path('contacts/', views.contacts_list, name='contacts_list'),
    path('contacts/create/', views.create_contact, name='create_contact'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contacts/<int:pk>/edit/', views.update_contact, name='update_contact'),
    path('contacts/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='delete_contact'),

    # URLs para experiencia
    path('work_experiences/', views.work_experience_list, name='work_experience_list'),
    path('work_experiences/create/', views.create_work_experience, name='create_work_experience'),
    path('work_experiences/<int:pk>/', views.work_experience_detail, name='work_experience_detail'),
    path('work_experiences/<int:pk>/edit/', views.update_work_experience, name='update_work_experience'),
    path('work_experiences/<int:pk>/delete/', views.WorkExperienceDeleteView.as_view(), name='delete_work_experience'),

    # URLs para formacao
    path('educations/', views.education_list, name='education_list'),
    path('educations/create/', views.create_education, name='create_education'),
    path('educations/<int:pk>/', views.education_detail, name='education_detail'),
    path('educations/<int:pk>/edit/', views.update_education, name='update_education'),
    path('educations/<int:pk>/delete/', views.EducationDeleteView.as_view(), name='delete_education'),
]
