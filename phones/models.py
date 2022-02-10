import datetime

from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256,  default='Phone')
    price = models.IntegerField(default=999999)
    image = models.URLField(max_length=400, default="https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/DynaTAC8000X.jpg/220px-DynaTAC8000X.jpg")
    release_date = models.DateField(default=datetime.date.fromisoformat('1973-04-03') )
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200)