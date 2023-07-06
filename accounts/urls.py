from django.urls import path
from . import views

app_name = 'hotel_accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('<str:username>/', views.profile, name='profile'),
]
