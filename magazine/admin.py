from django.contrib import admin
from .models import CategoriesList,Books
# Register your models here.
class CategoriesListRef(admin.ModelAdmin):
    list_display = ['category_name']
admin.site.register(CategoriesList,CategoriesListRef)
class BooksRef(admin.ModelAdmin):
    list_display = ['id','name','author','description','categorylist','subscription_cost','book_image']
admin.site.register(Books,BooksRef)
