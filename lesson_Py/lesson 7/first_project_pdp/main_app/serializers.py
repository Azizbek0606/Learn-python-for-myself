from rest_framework import serializers
from .models import Categories , Tags  ,Article


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