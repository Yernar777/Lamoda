from django.shortcuts import render
from .models import *
# Create your views here.
def lamoda(request):
    categoryes = Category.objects.all()
    return render(request,'index_lamoda.html',{'categoryes':categoryes})

def lamoda_category(request, id):
    product = LamodaCategory.objects.filter(category_id=id)
    return render(request, 'lamoda_category.html',{'product':product})