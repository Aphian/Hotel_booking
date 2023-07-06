from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index_board, name='index_board'),
    path('create/', views.create_board, name='create_board'),
    path('<int:board_pk>/', views.detail_board, name='detail_board'),
    path('<int:board_pk>/update/', views.update_board, name='update_board'),
    path('<int:board_pk>/delete/', views.delete_board, name='delete_board'),
]
