from django.contrib import admin
from .models import User, FriendDetails
from django.contrib.auth.admin import UserAdmin
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class FriendDetailsAdmin(admin.ModelAdmin):
    fields = ["friend_name",
              "friend_user_name",
              "rating",]
admin.site.register(FriendDetails, FriendDetailsAdmin)
admin.site.register(User, UserAdmin)
