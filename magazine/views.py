from django.shortcuts import render
from .models import CategoriesList,Books
# Create your views here.
def home(request):
     categories = CategoriesList.objects.all()
     books = Books.objects.all()
     #print(categories)
     return render(request, 'home.html',{'categories':categories,'books':books})