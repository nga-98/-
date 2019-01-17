from django.contrib import admin
from .models import Post
from .models import Picture
from django.contrib.auth.admin import UserAdmin

admin.site.register(Post)
admin.site.register(Picture)