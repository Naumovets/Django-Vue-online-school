from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'tel', 'vk_link', 'is_active', 'get_count_courses']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('image', 'first_name', 'last_name', 'tel', 'vk_link')}),
        ('Права', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важная информация', {'fields': ('last_login', 'date_joined')}),
    )

    @admin.display(description='Количество курсов')
    def get_count_courses(self, obj):
        return len(obj.order_courses.all())
