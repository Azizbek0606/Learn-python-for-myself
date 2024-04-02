from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, TagSerializer
from django.contrib import messages
from .forms import *

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
    tags = Tags.objects.all()
    data = {"categoryes": categoryes, "tags": tags}
    return render(request, "admin/add_article.html", context=data)


def add_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("context")
        author = request.user
        category_id = request.POST.get("category")
        tag_id = request.POST.get("tag")
        image = request.FILES.get("image")
        category = Categories.objects.get(id=category_id)
        tag = Tags.objects.get(id=tag_id)
        new_article = Article(
            title=title,
            content=content,
            author=author,
            category=category,
            image=image,
            tag=tag,
        )
        new_article.save()
        messages.success(request, "Maqola muvaffaqiyatli qo'shildi!")
        return redirect("/user/panel/")
    else:
        categories = Categories.objects.all()
        return render(request, "admin/add_article.html", {"categories": categories})


def admin_panel(request):
    all_article = Article.objects.all()
    data = {
        "article": all_article,
    }
    return render(request, "admin/delete_update.html", context=data)


def delete_this_article(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    messages.success(request, "Maqola muvaffaqiyatli o'chirildi!")
    return redirect("/user/panel/")


def article_update_view(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("/user/panel/", id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, "admin/update_article.html", {"form": form})
