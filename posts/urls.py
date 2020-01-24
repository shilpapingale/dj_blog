from django.urls import path
from . import views

# /post
urlpatterns = [
    path('', views.index)
]