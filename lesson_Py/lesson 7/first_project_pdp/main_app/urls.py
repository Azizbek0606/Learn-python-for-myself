from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.show_article, name="articles"),
    path("api/category/", views.CategoryListApi.as_view(), name="api_posts"),
    path("api/tag/", views.TagsListApi.as_view(), name="api_posts"),
    path(
        "api/article/", views.ArticleTitleListApi.as_view(), name="ArticleTitleListApi"
    ),
    path("add/article/", views.show_article_form, name="show_article_form"),
    path("add/article/form/", views.add_article, name="add_article"),
    path("user/panel/", views.admin_panel, name="admin_panel"),
    path(
        "delete/this/article/<id>",
        views.delete_this_article,
        name="delete_this_article",
    ),
    path("update/<id>", views.article_update_view, name="update_article"),
    path("search/", views.search_method, name="search"),
    path("by/tags/<id>" , views.filter_by_tags, name="filter_by_tags"),
]
