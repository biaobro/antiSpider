from django.urls import path
from section01 import views

urlpatterns = [
    path('lesson3_01', views.lesson3_01),
    path('lesson3_02', views.lesson3_02),
    path('lesson4_01', views.lesson4_01),
    path('lesson5_01', views.lesson5_01),
    path('lesson5_data_api', views.lesson5_data_api),
    path('lesson6_01', views.lesson6_01),
    path('lesson6_data_api', views.lesson6_data_api),
]