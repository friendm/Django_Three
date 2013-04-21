import csv

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from AT_Tracker.models import teacher,school

from Local_Settings import CSV_Location

class Command(BaseCommand):
    help = 'generates list of teachers from CSV'
    
    def handle(self, *args, **options):
        path = CSV_Location
        filename = '/Teacher_Name1.csv'
        path = path + filename
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
				First_Name = row[0],
				Last_Name = row[1],
				Middle_Name = row[2]
				School_Name = row[3]
				School_Location = row[4]
				School_1=school.objects.get(Name__iexact=School_Name,City__iexact=School_Location)
				#find the object in the database
				_, created = teacher.objects.get_or_create(
					First_Name = First_Name,
					Last_Name = Last_Name,
					Middle_Name = Middle_Name,
					School = School_1
					#uses the primary key of the school to add teacher object with foreign key
                    )
                # creates a tuple of the new object or
                # current object and a boolean of if it was created
				if not created:
					self.stderr.write('The Teacher "%s,%s,%s" already exists.' % (row[0],row[1],row[2]))
