from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# Create your views here.
from . models import HotelInfo

def hotel_info(request):
    return render(request, 'hotel_booking/info.html')



