from django.shortcuts import render
from django.views import generic
from .models import Room, Booking


class RoomList(generic.ListView):
    model = Room
    template_name = 'room_list.html'


class BookingList(generic.ListView):
    model = Booking
    template_name = 'booking_list.html'
