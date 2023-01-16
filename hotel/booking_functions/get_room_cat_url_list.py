from hotel.models import Room
from django.urls import reverse


def get_room_cat_url_list():
    """This will return the Room Category and Category URL List"""

    # Gets the "Room" object
    room = Room.objects.all()[0]

    # Creating a dictionary from "ROOM_CATEGORIES"
    room_categories = dict(room.ROOM_CATEGORIES)

    # Empty Room (Category, URL) List
    room_cat_url_list = []

    # Populating the room_list
    for category in room_categories:

        # room_category is Human Readable and category is Computer Readable.
        room_category = room_categories.get(category)
        room_url = reverse('hotel:RoomDetailView', kwargs={
                           'category': category})
        room_cat_url_list.append((room_category, room_url))

    return room_cat_url_list
