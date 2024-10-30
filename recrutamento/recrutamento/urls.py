from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('candidates.urls')),  # Inclui as URLs do app "candidates"
    path('api/', include('candidates.urls')),  # Inclui as rotas da API REST
]
