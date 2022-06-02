from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='app_2')
]
