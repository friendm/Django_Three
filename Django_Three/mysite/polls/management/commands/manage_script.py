from django.core.management.base import BaseCommand,CommandError
from django.core.management import call_command
import os

class Command(BaseCommand):
	args='filename'
	help='creates new sqlite database'
	
	def handle(self,*args,**options):
		path = '/home/michaelfriend/django_project/Django_Three/test_django_database.db'
		
		if os.path.exists(path):
			open(path,'w').close()
			call_command('syncdb',interactive=True)
		else:
			call_command('syncdb',interactive=True)
			
	
		
		
		



		
		
		
	
	
