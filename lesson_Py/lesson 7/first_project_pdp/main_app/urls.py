from django.urls import path
from . import views
app_name = "main_app"

urlpatterns = [
    path("", views.show_article, name="articles"),
    path("api/category/", views.CategoryListApi.as_view(), name="api_posts"),
    path("api/tag/", views.TagsListApi.as_view(), name="api_posts"),
    path("add/article", views.show_article_form, name="show_article_form"),
    path("add/article_form", views.add_article, name="add_article"),
]