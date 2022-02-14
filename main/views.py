from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os
from .models import Article, OfferedArticle
from .forms import ArticleOffer

def newspage(request):
    data = {
        "articles" : Article.objects.all()
    }
    return render(request, 'main/main.html', data)

def offerpage(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleOffer(request.POST)
        # check whether it's valid:
        if form.is_valid():
            OfferedArticle(name = form.cleaned_data['name'], image = form.cleaned_data['image'], info = form.cleaned_data['info'], is_accepted = False).save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/main.html')
    return render(request, 'main/offer.html')

def warning(request):
	return render(request, 'main/warning.pdf')

# def about(request):
# 	return render(request, 'main/about.html')
