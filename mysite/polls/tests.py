"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import timezone
from polls.models import Poll
import datetime

class PollMethodTest(TestCase):
   
	def test_published_recently_works(self):
		#tests if the was published recently takes into account future dates
		test_poll=Poll(pub_date=timezone.now()+datetime.timedelta(days=400))
		self.assertEqual(test_poll.was_published_recently(),False)
