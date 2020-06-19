from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.
#class HomeView(generic.ListView):
#    template_name = 'home/home.html'
    
def home(request):
    template_name = 'home/home.html'
    return render(request, template_name)#("Hello, world. You're at the polls index.")

