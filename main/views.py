from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import Article

def usermode(request):
    data = {
        "articles" : Article.objects.all()
    }
    return render(request, 'main/main.html', data)
