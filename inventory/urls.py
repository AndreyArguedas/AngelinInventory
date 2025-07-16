
from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('add/', views.product_create, name='product_create'),
    path('', views.intro_page, name='intro'),
    path('events/', views.event_list, name='event_list'),
    path('events/add/', views.event_create, name='event_create'),
]
