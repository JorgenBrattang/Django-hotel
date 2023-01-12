from django.urls import path
from .views import RoomListView, BookingList, BookingView, RoomDetail, RoomDetailView

app_name = 'hotel'

urlpatterns = [
    path('room_list/', RoomListView.as_view(), name='RoomList'),

    # Here for checking the html
    path('room_list/room_detail', RoomDetail.as_view(), name='RoomDetail'),


    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookingView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView')
]
