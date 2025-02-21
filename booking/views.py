from django.shortcuts import render, redirect
from .models import Room, Booking
from django.http import HttpResponse


def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms":rooms,
    }
    return render(request,"booking/room_list.html",context)


def room_details(request,pk):
    room = Room.objects.get(id=pk)
    context = {
        "room":room,
    }
    return render(request,"booking/room_details.html",context)


def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room_number")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        try:
            room = Room.objects.get(number=room_number)
        except Room.DoesNotExist:
            return HttpResponse("Room does not exist",status=404)
        booking = Booking.objects.create( 
            user=request.user,
            room=room,
            start_time=start_time,
            end_time=end_time
        )
        return redirect("booking_details",pk=booking.id)
    else:
        return render(request,"booking/booking_form.html")


def booking_details(request,pk):
    booking = Booking.objects.get(id=pk)
    context = {
        "booking":booking,
    }
    return render(request,"booking/room_details.html",context)