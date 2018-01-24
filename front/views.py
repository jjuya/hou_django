from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
import json

from .models import *
from .forms import *

# Create your views here.
def board_list(request):
    boards = Board.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'board/board_list.html', {'boards' : boards})

def board_detail(request, pk):
    board = get_object_or_404(Board, pk = pk)

    lists = List.objects.filter(board = board, created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'board/board_detail.html', {'board' : board, 'lists' : lists})

def board_new(request):
    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            board = form.save()

            return redirect('board_detail', pk=board.pk)
    else:
        form = BoardForm()

    return render(request, 'board/board_form.html', {'form' : form})

def board_edit(request, pk):
    board = get_object_or_404(Board, pk = pk)

    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)

        if form.is_valid():
            board = form.save()

            return redirect('board_detail', pk=board.pk)
    else:
        form = BoardForm(instance=board)

    return render(request, 'board/board_form.html', {'form' : form})

def board_destroy(request, pk):
    board = get_object_or_404(Board, pk = pk)
    board.delete()

    return redirect('board_list')

def list_new(request):
    if request.method == "POST":
        title  = request.POST.get('title')
        board = Board.objects.get(pk=request.POST.get('board_id'))
        created_date = timezone.now()

        new_list = List(title = title, board = board, created_date =  created_date)
        new_list.save()

    html = render_to_string('list/_list.html', {'list' : new_list})

    return HttpResponse(json.dumps(html), content_type='application/json')
