import csv

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from AT_Tracker.models import user,school

from Local_Settings import CSV_Location

class Command(BaseCommand):
    help = 'generates list of Grades from CSV'
    def handle(self, *args, **options):
        path = CSV_Location
        filename = '/users.csv'
        path = path + filename
        with open(path) as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                User_Name = row[0]
                Pass_word = row[1]
                School_Name = row[2]
                School_Location = row[3]
                School_1 = school.objects.get(Name__iexact=School_Name, City__iexact=School_Location)
                #find the object in the database
                _, created = user.objects.get_or_create(
                    Username=User_Name,
                    Password=Pass_word,
					School=School_1
                    #uses the primary key of the school 
                    #to add teacher object with foreign key
                    )
                # creates a tuple of the new object or
                # current object and a boolean of if it was created
                if not created:
					self.stderr.write('The Grade "%s,  already exists at %s, %s"' % (row[0], row[1], row[2]))

