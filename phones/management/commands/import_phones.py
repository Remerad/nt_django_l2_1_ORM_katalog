import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            for row in phones:
                print(row)
                Phone.objects.create(
                    id=row['id'],
                    name=row['name'],
                    price=row['price'],
                    release_date=row['release_date'],
                    image=row['image'],
                    lte_exists=row['lte_exists'],
                    slug=slugify(row['name'])
                )#id;name;image;price;release_date;lte_exists
