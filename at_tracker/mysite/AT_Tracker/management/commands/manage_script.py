from django.core.management.base import BaseCommand,CommandError
from django.core.management import call_command
import os
import sys
from Local_Settings import Counter

SETTINGS_PATH = os.path.abspath(__file__)
for i in range(Counter):
    SETTINGS_PATH = os.path.dirname(SETTINGS_PATH)
sys.path.insert(0, os.path.join(SETTINGS_PATH, 'mysite'))

print SETTINGS_PATH


from personal_settings import BASE_PATH

class Command(BaseCommand):
	args='filename'
	help='creates new sqlite database'
	
	def handle(self,*args,**options):
		path = BASE_PATH
		
		if os.path.exists(path):
			open(path,'w').close()
		call_command('syncdb',interactive=False)
			
	
		
		
		



		
		
		
	
	
