from django.urls import path
from users_app import views

urlpatterns = [
    path('medias/', views.media_list, name='media_list'),
]
