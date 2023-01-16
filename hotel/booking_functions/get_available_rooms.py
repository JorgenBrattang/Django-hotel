from hotel.models import Room
from .availability import check_availability


def get_available_rooms(category, check_in, check_out):
    """Function that takes category and returns Available Room List"""
    # Gets the queryset of the Rooms that match the category
    room_list = Room.objects.filter(category=category)

    # Starts a empty list for available_rooms
    available_rooms = []

    # Populates the available_rooms empty
    for room in room_list:
        if check_availability(room, check_in, check_out):
            available_rooms.append(room)

    # Check for length of the list
    if len(available_rooms) > 0:
        return available_rooms
    else:
        return None
