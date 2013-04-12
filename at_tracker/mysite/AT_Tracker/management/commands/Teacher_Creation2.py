import csv

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from AT_Tracker.models import teacher


class Command(BaseCommand):
    help = 'generates list of schools from csv'
    
    def handle(self, *args, **options):
        path = '/home/mike/python_projects/Django_3/django_projects'
        path = path + '/at_tracker/mysite/AT_Tracker/CSV_Files/'
        filename = 'Teacher_Name1.csv'
        path = path + filename
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = teacher.objects.get_or_create(
                    First_Name=row[0],
                    Last_Name=row[1],
                    Middle_Name=row[2],
                    School=row [3]
                    )
                # creates a tuple of the new object or
                # current object and a boolean of if it was created
                if not created:
                    self.stderr.write('The Teacher "%s,%s,%s" already exists.' % (row[0],row[1],row[2]))
