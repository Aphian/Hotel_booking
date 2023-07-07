from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
from . models import Book
from . forms import BookForm

from hotel_booking.models import HotelProduct, HotelInfo

User = get_user_model()

@login_required
@require_safe
def index_book(request):
    books = Book.objects.all()
    return render(request, 'booking/book_index.html', {
        'books' : books,
    })

@login_required
@require_http_methods(['GET', 'POST'])
def create_book(request, product_pk):
    if not request.user.groups.filter(name="client").exists():
        return redirect('home')

    if request.method == 'GET':
        book_form = BookForm()
    else:
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.user = request.user
            book.product_id = product_pk
            book.save()
            return redirect('booking:detail_book', book.pk, product_pk)
        
    return render(request, 'booking/book_form.html', {
        'book_form' : book_form,
    })

@require_safe
def detail_book(request, book_pk, product_pk):
    book = get_object_or_404(Book, pk=book_pk)
    product = get_object_or_404(HotelProduct, pk=product_pk)
    hotel = get_object_or_404(HotelInfo, pk=product.info_id)

    return render(request, 'booking/book_detail.html', {
        'book' : book,
        'product' : product,
        'hotel' : hotel,
    })

def update_book(requset, book_pk):
    pass

def cancle_book(requset, book_pk):
    pass
