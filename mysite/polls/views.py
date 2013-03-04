#Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("hello world, you are at the poll index")

def detail(request,poll_id):
	return HttpResponse("you are looking at poll %s.",% poll_id)

def vote(request,poll_id):
	return HttpRespnse("you'ee voting in poll %s", % poll_id)
