from hotel.models import Room


def get_room_category_human_format(category):
    """
    Function that takes the Computer format
    and returns the Human Readable format
    """
    room = Room.objects.all()[0]
    room_category = dict(room.ROOM_CATEGORIES).get(category, None)

    return room_category
