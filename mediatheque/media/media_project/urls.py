from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('membres/', views.liste_membres, name='liste_membres'),
    path('membres/creer/', views.creer_membre, name='creer_membre'),
    path('membres/modifier/<int:membre_id>/', views.update_membre, name='modifier_membre'), 
    path('membres/delete/<int:membre_id>/', views.delete_membre, name='delete_membre'),
    path('medias/', views.liste_medias, name='liste_medias'),
    path('add/livre/', views.add_livre, name='add_livre'),
    path('add/dvd/', views.add_dvd, name='add_dvd'),
    path('add/cd/', views.add_cd, name='add_cd'),
    path('add/jeu-de-plateau/', views.add_jeu_de_plateau, name='add_jeu_de_plateau'),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs d'authentification
]

