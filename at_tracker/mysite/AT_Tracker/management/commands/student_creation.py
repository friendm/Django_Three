import csv

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from AT_Tracker.models import grade,school,student

from Local_Settings import CSV_Location

from Data_Cleaner import string_clean
#string clean removes extra characters to allow for the removal of 

class Command(BaseCommand):
    help = 'generates list of students from CSV'
    
    def handle(self, *args, **options):
        path = CSV_Location
        filename = '/students.csv'
        path = path + filename
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
				First_Name = string_clean(row[0])
				Last_Name = string_clean(row[1])
				Middle_Name = string_clean(row[2])
				School_Name = row[3]
				School_Location = row[4]
				School_1=school.objects.get(Name__iexact=School_Name,City__iexact=School_Location)
				#finds the school object in the database
				Grade = string_clean(row[5])
				Grade_1=grade.objects.get(Grade_Level__exact=Grade,School=School_1)
				#finds the grade object in the database
				_, created = student.objects.get_or_create(
					First_Name = First_Name,
					Last_Name = Last_Name,
					Middle_Name = Middle_Name,
					School = School_1,
					Grade = Grade_1
                    )
                # creates a tuple of the new object or
                # current object and a boolean of if it was created
				if not created:
					self.stderr.write('The Student "%s,%s,%s" already exists at %s' % (row[0],row[1],row[2],School_1))
