#Create your views here.

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.template import Context,loader
from polls.models import Poll


def index(request):
	latest_poll_list=Poll.objects.order_by('-pub_date')[:2]
	template= loader.get_template('polls/first_template.html')
	context = Context({ 'latest_poll_list':latest_poll_list,
	})
	return HttpResponse(template.render(context))

def detail(request,poll_id):
	poll=get_object_or_404(Poll,pk=poll_id)
	return render(request,'polls/detail.html', {'poll':poll})

def vote(request,poll_id):
	return HttpResponse("you're voting in poll %s" % poll_id)
def results(request,poll_id):
	return HttpResponse("you're looking at the results of poll %s" % poll_id)


