from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='app_1'),
    path("app_1_1/",views.app_1_1, name='app_1_1'),
    path("app_1_2/",views.app_1_2, name='app_1_2'),
    path("app_1_3/",views.app_1_3, name='app_1_3'),
    path("app_1_4/",views.app_1_4, name='app_1_4'),
]
