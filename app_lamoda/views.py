from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render,redirect
# Create your views here.
def lamoda(request):
    categoryes = Category.objects.all()
    shapkyes = LamodaShapka.objects.all()
    shapkyes1 = LamodaShapka1.objects.all()
    return render(request,'index_lamoda.html',{'categoryes':categoryes,'shapkyes':shapkyes,'shapkyes1':shapkyes1})

def lamoda_category(request, id):
    product = LamodaCategory.objects.filter(category_id=id)
    return render(request, 'lamoda_category.html',{'product':product})


def review_functional(request):
    form1 = ReviewForms1()
    if request.method == 'POST':
        form1 = ReviewForms1(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('succes')
    else:
        form = ReviewForms()
    return render(request, 'forms.html',{'form': form, 'form1': form1,})