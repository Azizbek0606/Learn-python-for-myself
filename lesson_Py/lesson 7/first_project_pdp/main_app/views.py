from django.shortcuts import render, redirect
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Categories
from .serializers import CategorySerializer


# Create your views here.


class CategoryListApi(APIView):
    def get(self, request):
        category = Categories.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


def show_article(request):
    all_articles = Article.objects.all()
    data = {
        "article": all_articles,
    }
    return render(request, "index.html", context=data)


def show_article_form(request):
    categoryes = Categories.objects.all()
    data = {
        "categoryes": categoryes,
    }
    return render(request, "add_article.html" , context=data)


def add_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.user
        category = request.POST.get("category")
        new_article = Article(
            title=title, content=content, author=author, category=category
        )
        new_article.save()
        return redirect("/")
    else:
        return render(request, "add_article.html")
