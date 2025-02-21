from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')

def room_detail(request, room_id):
    return render(request, 'room_detail.html')

