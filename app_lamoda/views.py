from django.shortcuts import render
from .models import *
# Create your views here.
def lamoda(request):
    categoryes = Category.objects.all()
    shapkyes = LamodaShapka.objects.all()
    shapkyes1 = LamodaShapka1.objects.all()
    return render(request,'index_lamoda.html',{'categoryes':categoryes,'shapkyes':shapkyes,'shapkyes1':shapkyes1})

def lamoda_category(request, id):
    product = LamodaCategory.objects.filter(category_id=id)
    return render(request, 'lamoda_category.html',{'product':product})