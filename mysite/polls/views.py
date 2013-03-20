#Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.template import Context,loader
from polls.models import Choice,Poll
from django.core.urlresolvers import reverse
"""
def index(request):
	latest_poll_list=Poll.objects.order_by('-pub_date')[:2]
	template= loader.get_template('polls/first_template.html')
	context = Context({ 'latest_poll_list':latest_poll_list,
	})
	return HttpResponse(template.render(context))

def detail(request,poll_id):
	poll=get_object_or_404(Poll,pk=poll_id)
	return render(request,'polls/detail.html', {'poll':poll})
"""
def vote(request,poll_id):
	#this assigns the opject to p based on the value that is passed via the web url
	p=get_object_or_404(Poll,pk=poll_id)
	try:
		selected_choice=p.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
	#redisplays the poll voting form
		return render(request,"polls/vote.html",{'poll':p,'error_message':"You didn't select a choice",})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
"""
def results(request,poll_id):
	poll=get_object_or_404(Poll,pk=poll_id)
	return render(request,'polls/detail.html', {'poll':poll})

"""
