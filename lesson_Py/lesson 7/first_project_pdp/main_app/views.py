from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    return render(request, "index.html")





def show_article(request):
    all_articles = Article.objects.all()
    data = {
        "article": all_articles,
    }
    return render(request, "index.html", context=data)
