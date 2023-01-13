from django.urls import path
from .views import RoomListView, BookingListView, RoomDetailView

app_name = 'hotel'

urlpatterns = [
    path('room_list/', RoomListView, name='RoomListView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView')
]
