from django.shortcuts import render , redirect
from .models import *
# Create your views here.


def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    data = {"category": category,
            "products": products}
    return render(request, 'index.html' , context=data)


def filter_by_category(request):
    if request.method == "GET":
        into_category = request.GET.get("filter_by_category")
        if into_category:
            category = Category.objects.all()
            products = Product.objects.filter(category_id=into_category)
            return render(
                request,
                "index.html",
                context={"category": category, "products": products},
            )
        else:
            return redirect("/")
    else:
        return redirect("/")
