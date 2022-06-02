from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='app_2'),
    path("app_2_1/",views.app_2_1, name='app_2_1'),
    path("app_2_2/",views.app_2_2, name='app_2_2'),
    path("app_2_3/",views.app_2_3, name='app_2_3'),
    path("app_2_4/",views.app_2_4, name='app_2_4'),
]
