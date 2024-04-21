from django.urls import path
from . import views
app_name = "account"

urlpatterns = [
    path("user/login", views.login_view, name="login_method"),
    path("register/user/", views.login_method, name="login"),
    path("user/logout/" , views.logout_method , name="logout"),
    path("add/register/", views.signup_method, name="register"),
    # path("user/profile/" , views.profile_method , name="profile"),
    # path("user/edit/" , views.edit_method , name="edit"),
    # path("user/delete/" , views.delete_method , name="delete"),
]
