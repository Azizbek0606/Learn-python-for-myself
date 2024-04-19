from rest_framework import serializers
from .models import Categories , Tags  ,Article
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"

class ArticleTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["title" , 'content']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
