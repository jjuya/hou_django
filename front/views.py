from django.shortcuts import render

from .models import *

# Create your views here.
def board_list(request):
    boards = Board.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'board/board_list.html', {'boards' : boards})
