from django.contrib import admin
from .models import CategoriesList,Books
# Register your models here.
class CategoriesListRef(admin.ModelAdmin):
    list_display = ['category_name']
admin.site.register(CategoriesList,CategoriesListRef)
admin.site.register(Books)
