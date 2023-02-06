from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Person

# Create your views here.
def index(request):
  return HttpResponse('<h1>first build</h1>')


# def get_user_page(request, user_name):
#   return HttpResponse(f'<h1>{user_name}\'page</h1>')

# def get_number_page(request, number):
#   return HttpResponse(f'<h1>{number}\'page</h1>')


def get_all_persons(request):
  persons = Person.objects.all()
  return render(request, 'render_person.html', context={'persons': persons})

class PersonList(ListView):
  template_name = 'person_list.html'
  model = Person

class PersonDetail(DetailView):
  template_name = 'person_detail.html'
  model = Person

# class PersonCreate(CreateView):
#   template_name = 'person_create.html'
#   model = Person