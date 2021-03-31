from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("<h2 style='text-align:center;color:white;background-color:red'> welcome to homepage</h2>")


def chk(request):
	return HttpResponse("<script>alert('hi good afternoon')</script><h2>welcome</h2>")	


def haritha(request):
	return render(request,'charan/haritha.html')

def login(re):
	return render(re,'charan/login.html')

def ff(rt):
	return render(rt,'charan/ff.html')
	
