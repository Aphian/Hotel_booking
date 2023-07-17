from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.hotel_info, name='hotel_info'),
    path('search/', views.hotel_search, name="hotel_search"),

    path('create/', views.create_hotel_info, name='create_hotel_info'),
    path('<int:hotel_info_pk>/', views.detail_hotel_info, name='detail_hotel_info'),
    path('<int:hotel_info_pk>/update/', views.update_hotel_info, name='update_hotel_info'),
    path('<int:hotel_info_pk>/delete/', views.delete_hotel_info, name='delete_hotel_info'),

    path('<int:hotel_info_pk>/hotelreviews/create/', views.create_review, name='create_review'),
    path('<int:hotel_info_pk>/hotelreviews/delete/<int:hotel_review_pk>/', views.delete_review, name='delete_review'),

    path('<int:hotel_info_pk>/product/create', views.create_product, name='create_product'),
    path('<int:hotel_info_pk>/product/delete/<int:hotel_product_pk>/', views.delete_product, name='delete_product'),

    
]