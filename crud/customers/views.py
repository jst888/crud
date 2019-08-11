from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Crud

def home(request):
    Cruds =  Crud.objects
    return render(request, 'home.html', {'Cruds': Cruds})
