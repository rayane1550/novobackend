from django.urls import path
from . import views

urlpatterns = [
    path('pizza_do_dia/', views.pizza_do_dia, name='pizza_do_dia'),
    path('promocoes/', views.promocoes, name='promocoes'),
]
