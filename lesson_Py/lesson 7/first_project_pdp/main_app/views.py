from django.shortcuts import render, redirect
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Categories
from .serializers import CategorySerializer


# Create your views here.
def home(request):
    return render(request, "index.html")


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
