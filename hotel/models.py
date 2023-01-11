from django.db import models

# Create your models here.


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NO-AC'),
        ('LUX', 'LUXURY'),
        ('KIN', 'KING'),
        ('QEE', 'QUEEN'),
    )
    number = models.IntegerField()
    catergory = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return (f'{self.number}. {self.catergory} with {self.beds} bed(s) for {self.capacity} people')