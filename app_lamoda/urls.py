from django.urls import path
from .import views
from django.urls import path

urlpatterns = [
    path('',views.lamoda),
    path('lam/<int:id>',views.lamoda_category,name='lamoda_category'),
]