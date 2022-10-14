from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

from survey.admin import SurveyTitleInline


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'age']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    inlines = [
        SurveyTitleInline
    ]
