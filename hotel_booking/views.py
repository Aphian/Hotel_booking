from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# Create your views here.
from . models import HotelInfo, HotelReviews, HotelProduct
from . forms import HotelInfoForm, HotelReviewForm, HotelProductForm
from booking.models import Book

from django.db.models import Avg, Min

@require_safe
def hotel_info(request):
    hotel_infoes = HotelInfo.objects.all()

    return render(request, 'hotel_booking/hotel_info.html', {
        'hotel_infoes' : hotel_infoes,
    })

@login_required
@require_http_methods(['GET', 'POST'])
def create_hotel_info(request):
    if not request.user.groups.filter(name="register").exists():
        return redirect('home')

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
        'form' : create_form,
    })


@require_safe
def detail_hotel_info(request, hotel_info_pk):
    hotel_info = get_object_or_404(HotelInfo, pk=hotel_info_pk)
    reviews = hotel_info.reviews.all()
    products = hotel_info.products.all()
    score = 0.0
    price = 0
  
    avg_score = HotelReviews.objects.filter(info_id=hotel_info.pk).aggregate(avg_score=Avg("score"))
    min_price = HotelProduct.objects.filter(info_id=hotel_info.pk).aggregate(min_price=Min("price"))

    if avg_score['avg_score'] != None:
        score = avg_score['avg_score']

    if min_price['min_price'] != None:
        price = min_price['min_price']

    hotel_info.score = score
    hotel_info.price = price
    hotel_info.save()

    review_form = HotelReviewForm()
    return render(request, 'hotel_booking/hotel_detail.html', {
        'hotel_info' : hotel_info,
        'reviews' : reviews,
        'review_form' : review_form,
        'products' : products,
        'score' : score,
    })

@login_required
@require_http_methods(['GET', 'POST'])
def update_hotel_info(request, hotel_info_pk):
    hotel_info = get_object_or_404(HotelInfo, pk=hotel_info_pk)

    if request.user != hotel_info.user:
        return redirect('hotel:detail_hotel_info', hotel_info_pk)
    
    if request.method == 'GET':
        update_form = HotelInfoForm(instance=hotel_info)
    else:
        update_form = HotelInfoForm(request.POST, instance=hotel_info)
        if update_form.is_valid():
            hotel_info = update_form.save()
            return redirect('hotel:detail_hotel_info', hotel_info_pk)
        
    return render(request, 'hotel_booking/create_form.html', {
        'form' : update_form,
    })

@login_required
@require_POST
def delete_hotel_info(request, hotel_info_pk):
    hotel_info = get_object_or_404(HotelInfo, pk=hotel_info_pk)

    if request.user != hotel_info.user:
        return redirect('hotel:detail_hotel_info', hotel_info.pk)
    hotel_info.delete()

    return redirect('hotel:hotel_info')

@login_required
@require_POST
def create_review(request, hotel_info_pk):
    hotel_info = get_object_or_404(HotelInfo, pk=hotel_info_pk)

    review_form = HotelReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.info = hotel_info
        review.author = request.user
        review.save()
        return redirect('hotel:detail_hotel_info', hotel_info.pk)

@login_required
@require_POST
def delete_review(request, hotel_info_pk, hotel_review_pk):
    hotel_info = get_object_or_404(HotelInfo, pk=hotel_info_pk)
    hotel_review = get_object_or_404(HotelReviews, pk=hotel_review_pk)

    if request.user != hotel_review.author:
        return redirect('hotel:detail_hotel_info', hotel_info.pk)
    hotel_review.delete()

    return redirect('hotel:detail_hotel_info', hotel_info_pk)

@login_required
@require_http_methods(['GET', 'POST'])
def create_product(request, hotel_info_pk):
    hotel_info = get_object_or_404(HotelInfo, pk=hotel_info_pk)

    if request.method == 'GET':
        product_form = HotelProductForm()

    else:
        product_form = HotelProductForm(request.POST)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.info = hotel_info
            product.user = request.user
            product.save()
            return redirect('hotel:detail_hotel_info', hotel_info.pk)
    
    return render(request, 'hotel_booking/product_form.html', {
        'products_form' : product_form,
    })

@login_required
@require_POST
def delete_product(request, hotel_info_pk, hotel_product_pk):
    hotel_info = get_object_or_404(HotelInfo, pk=hotel_info_pk)
    hotel_product = get_object_or_404(HotelProduct, pk=hotel_product_pk)

    if request.user != hotel_product.user:
        return redirect('hotel:detail_hotel_info', hotel_info.pk)
    
    hotel_product.delete()

    return redirect('hotel:detail_hotel_info', hotel_info.pk)
