from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'hotel_accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('<str:username>/', views.profile, name='profile'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)