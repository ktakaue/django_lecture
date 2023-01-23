from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Person

# Create your views here.
def index(request):
  return HttpResponse('<h1>first build</h1>')

# def get_user_page(request, user_name):
#   return HttpResponse(f'<h1>{user_name}\'page</h1>')

# def get_number_page(request, number):
#   return HttpResponse(f'<h1>{number}\'page</h1>')

class PersonList(ListView):
  template_name = 'person_list.html'
  model = Person