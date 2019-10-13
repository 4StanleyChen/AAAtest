from django.shortcuts import render
from datetime import datetime
import socket


# Create your views here.

def easytry(request):
    context = {'first_line': '現在時間：', 'second_line': datetime.now(),
               'third_line': '當前位置：', 'fourth_line':  socket.gethostbyname(socket.gethostname())}

    return render(request, 'easytry.html', context=context)
