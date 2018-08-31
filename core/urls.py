from django.urls import path
from . import  views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('about/', views.about, name="about"),
    path('contacto/', views.contact, name="contacto"),
    path('blog/', views.blog, name="blog"),
    path('store/', views.store, name="store"),
    path('sample/', views.store, name="sample"),

]