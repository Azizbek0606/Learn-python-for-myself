from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "chat"

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),
]
