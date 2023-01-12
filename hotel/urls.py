from django.urls import path
from .views import RoomList, BookingList, BookingView, RoomDetail

app_name = 'hotel'

urlpatterns = [
    path('room_list/', RoomList.as_view(), name='RoomList'),
    path('room_list/room_detail', RoomDetail.as_view(), name='RoomDetail'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookingView')
]
