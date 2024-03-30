from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main_app.urls", namespace="main_app")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
