from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
import json

from .models import *
from .forms import *

# views : board
def board_list(request):
    boards = Board.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'board/board_list.html', {'boards' : boards})

def board_detail(request, pk):
    board = get_object_or_404(Board, pk = pk)

    # lists = List.objects.filter(board = board, created_date__lte=timezone.now()).order_by('created_date')
    lists = board.list_set.all()

    return render(request, 'board/board_detail.html', {'board' : board, 'lists' : lists})

def board_new(request):
    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            board = form.save()

            new_list = List(title="No title", board = board, created_date = timezone.now())
            new_list.save()

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


# views : list
def list_new(request):
    if request.method == "POST":
        title  = request.POST.get('title')
        board = Board.objects.get(pk=request.POST.get('board_id'))
        created_date = timezone.now()

        new_list = List(title = title, board = board, created_date =  created_date)
        new_list.save()

    html = render_to_string('list/_list.html', {'list' : new_list})

    return HttpResponse(json.dumps(html), content_type='application/json')

def list_edit(request, pk):
    edit_list = get_object_or_404(List, pk = pk)

    if request.method == "POST":
        form = ListForm(request.POST, instance=edit_list)

        if form.is_valid():
            edit_list = form.save()

            return redirect('board_detail', pk=edit_list.board.pk)
    else:
        form = ListForm(instance=edit_list)

    return render(request, 'list/list_form.html', {'form' : form})

def list_destroy(request, pk):
    del_list = get_object_or_404(List, pk = pk)
    board_id = del_list.board.pk

    if del_list.title != "No title":
        del_list.delete()
    else:
        message = "You don't destroy this list"

    return redirect('board_detail', pk=board_id)

# views : bookmark
def bookmark_new(request):

    if request.method == "POST":
        form = BookmarkForm(request.POST)

        if form.is_valid():
            bookmark = form.save()

            return redirect('board_detail', pk=bookmark.list.board.pk)
    else:
        form = BookmarkForm()

    return render(request, 'bookmark/bookmark_form.html', {'form' : form})

def bookmark_edit(request, pk):
    edit_bookmark = get_object_or_404(Bookmark, pk = pk)

    if request.method == "POST":
        form = BookmarkForm(request.POST, instance=edit_bookmark)

        if form.is_valid():
            edit_bookmark = form.save()

            return redirect('board_detail', pk=edit_bookmark.list.board.pk)
    else:
        form = BookmarkForm(instance=edit_bookmark)

    return render(request, 'bookmark/bookmark_form.html', {'form' : form})

def bookmark_destroy(request, pk):
    del_bookmark = get_object_or_404(Bookmark, pk = pk)
    board_id = del_bookmark.list.board.pk

    del_bookmark.delete()


    return redirect('board_detail', pk=board_id)
