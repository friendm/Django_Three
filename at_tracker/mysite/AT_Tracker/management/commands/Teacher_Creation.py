import csv

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from AT_Tracker.models import school

from Local_Settings import CSV_Location

class Command(BaseCommand):
    help = 'generates list of schools from csv'
    
    def handle(self, *args, **options):
        path = CSV_Location
        filename = '/Schools_List.csv'
        path = path + filename
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = school.objects.get_or_create(
                    Name=row[0],
                    City=row[1])
                # creates a tuple of the new object or
                # current object and a boolean of if it was created
                if not created:
                    self.stderr.write('The school "%s" already exists.' % row[0])

