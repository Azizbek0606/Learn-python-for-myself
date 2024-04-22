from django.shortcuts import render, redirect
from .models import Message 


def chatPage(request):
    if not request.user.is_authenticated:
        return redirect("/login/user/login")
    messages = Message.objects.all()
    context = {"messages": messages}
    return render(request, "chat/chat_page.html", context)
