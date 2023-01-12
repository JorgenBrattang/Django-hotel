from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Room, Booking
from .forms import AvailabiltyForm
from hotel.booking_functions.availability import check_availability


class RoomList(ListView):
    model = Room
    template_name = 'room_list.html'


class RoomDetail(ListView):
    model = Room
    template_name = 'detail.html'


class BookingList(ListView):
    model = Booking
    template_name = 'booking_list.html'


class BookingView(FormView):
    form_class = AvailabiltyForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(catergory=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('No more free rooms of this category are left at this time.')
