from audioop import reverse
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ConnexionForm


def index(request):
    return render(request, 'index.html')

def profil(request):
    return render(request, 'profil.html')


def submit_edition_user(request, p_id):

    user = get_object_or_404(User, pk=p_id)
    if request.method == 'POST':
        user.email = request.POST["email"]
        user.save()
        return render(request, 'profil.html')
    else:
        return render(request, 'profil.html')


# Create your views here.
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print "Logged in"
            return HttpResponseRedirect(reverse('profil'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def connexion(request):
    #error = False
    username = request.POST['username']
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return render(request, 'profil.html')
    else:
        return render(request, 'index.html')


def deconnexion(request):
    logout(request)
    return render(request, 'index.html')