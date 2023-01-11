# Installing frameworks / libaries
## Django and gunicorn
```
pip3 install 'django<4' gunicorn
```
*gunicorn is the server we are using to run Django on Heroku.*

## Control our database
```
pip3 install dj_database_url==0.5.0 psycopg2
```

## Cloudinary for our storage of static files
```
pip3 install dj3-cloudinary-storage
```

## Install Bootstrap
```
pip install crispy-bootstrap5
```

## Requirements.txt file
This needs to be updated as soon as a new framework / libary is installed.
```
pip3 freeze --local > requirements.txt
```

## Django Shortcuts
```
pip install django-shortcuts
```

# Start the project in Django
```
django-admin startproject DjangoHotel .
```
*the dot here is so we create it in the current folder.*

## Create an app for our project
```
python3 manage.py startapp hotel
```

## Models
```python
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
```