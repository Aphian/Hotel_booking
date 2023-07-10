from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('<str:username>/', views.index_book, name='book_index'),
    path('<int:product_pk>/create/', views.create_book, name='create_book'),
    path('<int:book_pk>/detail/<int:product_pk>/', views.detail_book, name='detail_book'),
    path('<int:book_pk>/update/<int:product_pk>/', views.update_book, name='update_book'),
    path('<int:book_pk>/cancle/<int:product_pk>/', views.cancle_book, name='cancle_book'),
    path('<int:book_pk>/delete/<int:product_pk>/', views.delete_book, name='delete_book')
]
