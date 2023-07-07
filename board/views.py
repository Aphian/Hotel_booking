from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# Create your views here.
from . models import AdminBoard
from . forms import AdminBoardForm

# Create your views here.

@require_safe
def index_board(request):
    boards = AdminBoard.objects.order_by('updated_at')

    return render(request, 'board/index.html', {
        'boards' : boards,
    })

@login_required
@require_http_methods(['GET', 'POST'])
def create_board(request):
    if not request.user.groups.filter(name="adminpage").exists():
        return redirect('home')

    if request.method == 'GET': 
        board_form = AdminBoardForm()
    else:
        board_form = AdminBoardForm(request.POST)
        if board_form.is_valid():
            board = board_form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('board:detail_board', board.pk)
        
    return render(request, 'board/create_board.html', {
        'board_form' : board_form,
    })

@require_safe
def detail_board(request, board_pk):
    board = get_object_or_404(AdminBoard, pk=board_pk)

    board.views += 1
    board.save()

    return render(request, 'board/detail_board.html', {
        'board' : board,
    })

@login_required
@require_http_methods(['GET', 'POST'])
def update_board(request, board_pk):
    board = get_object_or_404(AdminBoard, pk=board_pk)

    if request.user != board.user:
        return redirect('board:feed_detail', board_pk)
    
    if request.method == 'GET':
        update_board_form = AdminBoardForm(instance=board)
    else:
        update_board_form = AdminBoardForm(request.POST, instance=board)
        if update_board_form.is_valid():
            board = update_board_form.save()
            return redirect('board:detail_board', board_pk)
        
    return render(request, 'board/create_board.html', {
        'board_form' : update_board_form,
    })

@login_required
@require_POST
def delete_board(request, board_pk):
    board = get_object_or_404(AdminBoard, pk=board_pk)

    if request.user != board.user:
        return redirect('board:detail_board', board.pk)
    board.delete()

    return redirect('board:index_board')