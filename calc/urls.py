from django.urls import path
from . import views


urlpatterns = [
    path('addnum', views.addnum, name='addnum'),

    path('', views.home, name='home')
]