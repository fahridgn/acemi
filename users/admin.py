from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreaitonForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
