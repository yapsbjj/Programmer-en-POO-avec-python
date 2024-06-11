from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('membres/', views.liste_membres, name='liste_membres'),
    path('membres/creer/', views.creer_membre, name='creer_membre'),
    path('medias/', views.liste_medias, name='liste_medias'),
]
