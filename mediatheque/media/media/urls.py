from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('media_project.urls')),
    path('users_app/', include('users_app.urls')),
]
