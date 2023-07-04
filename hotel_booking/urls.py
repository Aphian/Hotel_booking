from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.hotel_info, name='hotel_info'),
    path('create/', views.create_hotel_info, name='create_hotel_info'),
    path('<int:hotel_info_pk>/', views.detail_hotel_info, name='detail_hotel_info'),
]