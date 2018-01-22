from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *

# Create your views here.
def board_list(request):
    boards = Board.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'board/board_list.html', {'boards' : boards})

def board_detail(request, pk):
    board = get_object_or_404(Board, pk = pk)

    return render(request, 'board/board_detail.html', {'board' : board})

def board_new(request):
    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            board = form.save()

            return redirect('board_detail', pk=board.pk)
    else:
        form = BoardForm()

    return render(request, 'board/board_new.html', {'form' : form})
