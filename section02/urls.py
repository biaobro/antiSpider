from django.urls import path
from section02 import views

urlpatterns = [
    path('lesson1_server_time', views.lesson1_server_time),

    path('lesson1_01', views.lesson1_01),
    path('lesson1_01_data_api', views.lesson1_01_data_api),

    path('lesson1_02', views.lesson1_02),
    path('lesson1_02_data_api', views.lesson1_02_data_api),

    path('lesson1_03', views.lesson1_03),
    path('lesson1_03_data_api', views.lesson1_03_data_api),
]