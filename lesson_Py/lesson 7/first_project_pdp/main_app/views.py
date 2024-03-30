from django.shortcuts import render, redirect
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer , TagSerializer
from django.contrib import messages


# Create your views here.


class CategoryListApi(APIView):
    def get(self, request):
        category = Categories.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class TagsListApi(APIView):
    def get(self, request):
        tag = Tags.objects.all()
        serializer = TagSerializer(tag, many=True)
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
    return render(request, "add_article.html", context=data)


def add_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("context")
        author = request.user
        category_id = request.POST.get("category")
        image = request.FILES.get("image")
        category = Categories.objects.get(id=category_id)
        new_article = Article(
            title=title, content=content, author=author, category=category, image=image
        )
        new_article.save()
        messages.success(request, "Maqola muvaffaqiyatli qo'shildi!")
        return redirect("/")
    else:
        categories = Categories.objects.all()
        return render(request, "add_article.html", {"categories": categories})
