from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# Create your views here.
from . models import HotelInfo, HotelReviews
from . forms import HotelInfoForm, HotelReviewForm

@require_safe
def hotel_info(request):
    hotel_infoes = HotelInfo.objects.all()
    return render(request, 'hotel_booking/hotel_info.html', {
        'hotel_infoes' : hotel_infoes
    })

@login_required
@require_http_methods(['GET', 'POST'])
def create_hotel_info(request):
    if request.method == 'GET':
        create_form = HotelInfoForm()
    else:
        create_form = HotelInfoForm(request.POST)
        if create_form.is_valid():
            hotel_info = create_form.save(commit=False)
            hotel_info.user = request.user
            hotel_info.save()
            return redirect('hotel:detail_hotel_info', hotel_info.pk)
    return render(request, 'hotel_booking/create_form.html', {
        'create_form' : create_form,
    })

@require_safe
def detail_hotel_info(request, hotel_info_pk):
    hotel_info = get_object_or_404(HotelInfo, pk=hotel_info_pk)

    return render(request, 'hotel_booking/hotel_detail.html', {
        'hotel_info' : hotel_info,
    })




