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

    path('lesson2_01', views.lesson2_01),
    path('lesson2_01_data_api', views.lesson2_01_data_api),

    path('lesson3_01', views.lesson3_01),
    path('lesson3_01_data_api', views.lesson3_01_data_api),

    path('lesson4_01', views.lesson4_01),
    # path('lesson4_01_data_api', views.lesson4_01_data_api),
]