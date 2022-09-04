from dataclasses import fields
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangedForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangedForm
    model = User
    list_display = ('email','is_staff','is_active',)
    list_filter = ('email','is_staff','is_active',)
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Permissions',{'fields':('is_staff','is_active')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_staff','is_active')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    # fieldsets = (
    #     UserAdmin.fieldsets,
    #     (
    #         'custom Fieldset Heading',
    #         {
    #             'fields':(
    #                 'is_bot_flag',
    #             ),
    #         },
    #     ),
    # )

# admin.site.unregister(User)
admin.site.register(User)