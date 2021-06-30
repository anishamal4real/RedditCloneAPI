from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

fields = list(UserAdmin.fieldsets)
UserAdmin.fieldsets = tuple(fields)


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Post)
admin.site.register(Vote)

