import csv
import itertools # allows iteration over CSV files

import os
import sys

BASE_PATH = os.path.abspath(__file__)
for i in range(4):
    BASE_PATH = os.path.dirname(BASE_PATH)
sys.path.insert(0, os.path.join(BASE_PATH, 'lib'))
#allows for acess to the location of django module

from at_tracker import models
# importing school object

with open('Schools_List.csv', 'rb') as f:
	reader =csv.reader(f)
	
	for row in reader:
		School_Name = row[0]
		School_City = row[1]
		p=School() # instantiates a school object
		if p.is_unique(School_Name,School_City):#checks if values are unique
			p.Name = School_Name
			p.City = School_City
			p.save()
		else:
			print "This school name" + School_Name + " already exists in the system for the city" + School_City
		
