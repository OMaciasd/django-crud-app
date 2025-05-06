from django.shortcuts import render
from .models import UserProfile

def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})
