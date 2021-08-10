from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Hall, Video
from .forms import VideoForm, SearchForm
from django.contrib.auth import authenticate, login
from django.http import Http404, JsonResponse
from django.forms.utils import ErrorList
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import urllib
import requests





YOUTUBE_API_KEY = 'AIzaSyCTTaNaHjzPE906-oTBe0l8DIN_4z5p3E4'

def home(request):
    recent_halls = Hall.objects.all().order_by('-id')[:3]
    popular_halls = []
    return render(request, 'halls/home.html', {'recent_halls':recent_halls, 'popular_halls':popular_halls})
