from django.contrib import admin
from django.forms import Textarea

from .models import NewUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = NewUser

    search_fields = ('email', 'user_name', 'first_name')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Personal', {'fields': ('last_name', 'phone_number')}),
        ('Permissions', {'fields':('is_staff', 'is_active')}),
    )


    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'referral_code', 'bitcoin_wallet_address',
                       'phone_number', 'next_of_kin', 'next_of_kin_phone_number', 'password1', 'password2', 'is_active', 'is_staff')
        })
    )

admin.site.register(UserAdminConfigure)