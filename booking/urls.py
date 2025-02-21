from django.urls import path,include
from .views import room_list,room_details,book_room,booking_details
urlpatterns = [
    path('', room_list, name="room_list"),
    path('<int:pk>/',room_details,name="room_details"),
    path('book_room/',book_room,name="book_room"),
    path('booking_<int:pk>/',booking_details,name="booking_details"),

]
