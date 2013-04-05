import csv

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from AT_Tracker.models import School


class Command(BaseCommand):
    help = 'generates list of schools from csv'
    
    def handle(self, *args, **options):
        path = args[0]
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = School.objects.get_or_create(
                    name=row[0],
                    city=row[1])
                # creates a tuple of the new object or
                # current object and a boolean of if it was created
                if not created:
                    self.stderr.write('The school "%s" already exists.' % row[0])

