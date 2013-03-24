import csv
import itertools

with open('Schools_List.csv', 'rb') as f:
	reader =csv.reader(f)
	
	for row in reader:
		Name = row[0]
		City = row[1]
		print row
		print Name + "--" + City
