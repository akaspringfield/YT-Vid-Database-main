from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Hall, Video

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import urllib
import requests





YOUTUBE_API_KEY = 'AIzaSyCTTaNaHjzPE906-oTBe0l8DIN_4z5p3E4'

def home(request):
    recent_halls = Hall.objects.all().order_by('-id')[:3]
    popular_halls = []
    return render(request, 'halls/home.html', {'recent_halls':recent_halls, 'popular_halls':popular_halls})

@login_required
def dashboard(request):
    halls = Hall.objects.filter(user=request.user)
    return render(request, 'halls/dashboard.html', {'halls':halls})

@login_required
def add_video(request, pk):
    form = VideoForm()
    search_form = SearchForm()
    hall =  Hall.objects.get(pk=pk)
    if not hall.user == request.user:
        raise Http404

    if request.method == 'POST':
        form = VideoForm(request.POST)
       

    return render(request, 'halls/add_video.html', {'form':form,'search_form':search_form, 'hall':hall})



