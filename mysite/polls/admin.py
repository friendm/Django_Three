from polls.models import Poll
from django.contrib import admin
from polls.models import Choice

class ChoiceInLine(admin.TabularInline):
	model=Choice
	extra = 3


class PollAdmin(admin.ModelAdmin):
	fieldsets=[
	
	(None, {'fields':['question']}),
	('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
	]
	inlines=[ChoiceInLine]
	
	list_display=('question','pub_date')
	
admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)

