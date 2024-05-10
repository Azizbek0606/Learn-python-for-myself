from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path("" , home , name='home'),
    path("employee/" , employee , name='employee'),
    path("news/" , news , name='news'),
    path("contact/" , contact , name='contact'),
]
