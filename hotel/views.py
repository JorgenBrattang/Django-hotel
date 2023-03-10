from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Room, Booking
from .forms import AvailabiltyForm

# Importing functions to shortening the code
from hotel.booking_functions.availability import check_availability
from hotel.booking_functions.get_room_cat_url_list import get_room_cat_url_list
from hotel.booking_functions.get_room_category_human_format import get_room_category_human_format
from hotel.booking_functions.get_available_rooms import get_available_rooms
from hotel.booking_functions.book_room import book_room


def RoomListView(request):
    room_category_url_list = get_room_cat_url_list()

    context = {
        'room_list': room_category_url_list,
    }
    return render(request, 'room_list_view.html', context)


class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list_view.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        # Checks if the user is staff
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list

        # Or normal user
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        # Get room category from kwargs
        category = self.kwargs.get('category', None)

        # Get the human readable format
        human_format_room_category = get_room_category_human_format(category)

        # Starts the empty form
        form = AvailabiltyForm()

        # Check for invalid category names
        if human_format_room_category is not None:
            context = {
                'room_category': human_format_room_category,
                'form': form,
            }
            return render(request, 'room_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        # Get room category from kwargs
        category = self.kwargs.get('category', None)

        # Gets the form thats being POST:ed
        form = AvailabiltyForm(request.POST)

        # Confirms if the form is valid and gets the cleaned data
        if form.is_valid():
            data = form.cleaned_data

        # Get the available rooms
        available_rooms = get_available_rooms(category, data['check_in'], data['check_out'])

        # Check if the room are available
        if available_rooms is not None:

            # Book the first available room in the list
            booking = book_room(request, available_rooms[0], data['check_in'], data['check_out'])
            context = {
                'booking': booking
            }
            return render(request, 'success_booking.html', context)
        else:
            context = {
                'data': data
            }
            return render(request, 'no_more_rooms.html', context)


class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('hotel:BookingListView')
