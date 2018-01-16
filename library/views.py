from django.shortcuts import render, redirect

def index(request):
	template_name = 'library/index.html'
	return render(request, template_name, context={
		    'page_name': 'Home',
		})