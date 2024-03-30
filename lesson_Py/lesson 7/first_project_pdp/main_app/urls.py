from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.show_article, name="articles"),
    path("category", views.category, name="category")
]
