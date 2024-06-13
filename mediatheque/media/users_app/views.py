from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from media_project.models import Media

def is_borrower(user):
    return user.groups.filter(name='emprunteurs').exists()

@login_required
@user_passes_test(is_borrower)
def media_list(request):
    medias = Media.objects.all()
    return render(request, 'users_app/media_list.html', {'medias': medias})
