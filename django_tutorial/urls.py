from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('room/', views.room),
    path('room/<int:room_id>/', views.room_detail)
]