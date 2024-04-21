from django.shortcuts import render, redirect


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("/login/user/login")
    context = {}
    return render(request, "chat/chat_page.html", context)
