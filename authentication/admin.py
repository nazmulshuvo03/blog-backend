from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'profile_image')
    list_filter = ('updated_date', 'created_date', 'is_staff', 'is_active', 'is_admin', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name', 'username')
    actions = ['active_all', 'deactive_all']

    def active_all(self, request, queryset):
        queryset.update(is_active=True)

    def deactive_all(self, request, queryset):
        queryset.update(is_active=False)