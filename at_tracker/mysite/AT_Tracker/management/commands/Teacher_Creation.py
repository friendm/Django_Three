from django.core.management.base import BaseCommand, CommandError
import csv
import itertools # allows iteration over CSV files

import os
import sys

sys.dont_write_bytecode = True

from AT_Tracker.models import *

class Command(BaseCommand):
    
    help = 'generates list of schools from csv'
    
    def handle(self, *args, **options):
        with open("/home/mike/python_projects/Django_3/django_projects/at_tracker/mysite/AT_Tracker/CSV_Files/Schools_List.csv", 'rb') as f:
            reader =csv.reader(f)
            for row in reader:
                School_Name = row[0]
                School_City = row[1]
                p,created = Schools.objects.get_or_create(Name=School_Name,City=School_City) 
                # creates a tupple of the new object or current object and a boolean of if it was created
                if created == False:
                    print "the following school name: " + School_Name + " is a duplicate value in: " + School_City

