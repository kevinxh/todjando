from datetime import datetime
from django.shortcuts import render

def hello_world(request):
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })
