from django.core.management.base import BaseCommand, CommandError
import csv
import itertools # allows iteration over CSV files

import os
import sys

sys.dont_write_bytecode = True

from AT_Tracker.models import *

"""BASE_PATH = os.path.abspath(__file__)
for i in range(4):
    BASE_PATH = os.path.dirname(BASE_PATH)
sys.path.insert(0, os.path.join(BASE_PATH, 'lib'))
#allows for acess to the location of django module
"""


class Command(BaseCommand):
	
	help = 'generates list of schools from csv'
	
	def handle(self, *args, **options):
		
	
		
		with open("/home/mike/python_projects/Django_3/django_projects/at_tracker/mysite/AT_Tracker/management/commands/Schools_List.csv", 'rb') as f:
			reader =csv.reader(f)
			print "got here"
			p = Schools()
			for row in reader:
				School_Name = row[0]
				School_City = row[1]
			
				print School_Name
				print School_City
					
				if p.is_unique(School_Name,School_City):#checks if values are unique
					p.Name = School_Name
					
					print p.Name
					p.City = School_City
					p.save()
				else:
					print "This school name" + School_Name + " already exists in the system for the city" + School_City
			

