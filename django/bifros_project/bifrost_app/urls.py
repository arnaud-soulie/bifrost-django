from bifrost_app import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('add_volume/', views.add_volume),
]
