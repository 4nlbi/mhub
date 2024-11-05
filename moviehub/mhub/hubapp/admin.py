from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Category, Movie

# Customizing Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'desc')  # Fields to display in the list view
    prepopulated_fields = {'slug': ('name',)}  # Auto-populate the slug field from the name

# Customizing Movie Admin
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_year', 'category', 'rating', 'added_by')  # Fields to display
    list_filter = ('category', 'release_year')  # Filters to the right sidebar
    search_fields = ('name', 'description')  # Searchable fields

# Customizing User Admin
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')  # Fields to display
    search_fields = ('username', 'email')  # Searchable fields

# Unregister the default User admin and register the custom one
admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, UserAdmin)  # Register the custom User admin

# Register your models with the customized admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)
