from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import (
    CategorySerializer,
    TagSerializer,
    ArticleTitleSerializer,
    UserSerializer,
)
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
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


class ArticleTitleListApi(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleTitleSerializer(article, many=True)
        return Response(serializer.data)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
        messages.success(request, "Article saved successfully")
        return redirect("/user/panel/")
    else:
        messages.error(request, "Something went wrong")
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
    messages.success(request, "Article deleted successfully")
    return redirect("/user/panel/")


def article_update_view(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article was successfully updated")
            return redirect("/user/panel/", id=article.id)
    else:
        messages.error(request, "Something went wrong")
        form = ArticleForm(instance=article)
    return render(request, "admin/update_article.html", {"form": form})


def search_method(request):
    if request.method == "GET":
        query = request.GET.get("search")
        answer = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        if answer:
            messages.success(request, f"'{len(answer)}' article was found")
        else:
            messages.info(request, "article was not found")
    data = {"article": answer}
    return render(request, "index.html", context=data)


def filter_by_tags(request, id):
    answer = Article.objects.filter(tag__id=id)
    data = {"article": answer}
    return render(request, "index.html", context=data)


def filter_by_category(request, id):
    answer = Article.objects.filter(category__id=id)
    data = {"article": answer}
    return render(request, "index.html", context=data)


def details(request, id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=article)
    data = {"article": article,
            "comments": comments}
    return render(request, "detail.html", context=data)


def add_comment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        comment_text = request.POST.get("comment")
        author = request.user
        new_comment = Comment(comment=comment_text, author=author, article=article)
        new_comment.save()
        article.comments += 1
        article.save()
        messages.success(request, "Comment saved successfully")
        return redirect(f"/details/{id}")
    else:
        messages.error(request, "Something went wrong")
        return render(request, "detail.html", {"article": article})


def login_method(request):
    # if request.method == "POST":
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect("/user/panel/")
    #     else:
    #         messages.error(request, "Wrong username or password")
    return render(request, "register/login.html")
