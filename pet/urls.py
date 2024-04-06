"""Linking urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='show'),
    path('addpet/', views.addpet, name='addpet'),
    path('details/<petid>', views.details, name='details'),
    path('update/<petid>', views.update, name='update'),
    path('delete/<petid>',views.delete, name='delete'),
    path('contact/', views.contact, name='contact'),
]
# to access dog you would go to pet/
