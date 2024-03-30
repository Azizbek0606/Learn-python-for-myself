from django.contrib import admin
from .models import *

admin.site.register(Categories)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(View)
admin.site.register(Tags)