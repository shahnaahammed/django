from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

#def contact(request):return HttpResponse('<h1> Student IT Services - contact </h1>')


def home(request):
    return render(request, 'itreporting/home.html')

def about(request):
    return render(request, 'itreporting/about.html')

def contact(request):
    return render(request, 'itreporting/contact.html')

