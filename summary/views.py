from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Course, PetProject


def my_age():
    """this function shows my age today"""

    today = date.today()
    birthday = date(year=today.year, month=5, day=18)
    birthdate = date(year=1996, month=5, day=18)
    
    age = today.year - birthdate.year
    if today >= birthday:
        return age
    else:
        return age - 1


class Home(ListView):
    model = Course
    template_name = 'summary/index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_projects'] = PetProject.objects.order_by('id')
        context['date_of_birth'] = date(year=1996, month=5, day=18)
        context['age'] = my_age()
        context['my_photo'] = 'ICY-mAf5sYY.jpg'
        context['stack'] = ('Python 3', 'Django', 'PostgreSQL', 'GIT', 'html, css (базовый уровень)', )
        return context
    
    

