from calendar import month
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Course, PetProject

# Create your views here.
# def index(request):
#     template = 'summary/index.html'
#     context = {
#         'my_photo': 'ICY-mAf5sYY.jpg',
#     }
#     return render(request, template_name=template, context=context)

class Home(ListView):
    model = Course
    template_name = 'summary/index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_projects'] = PetProject.objects.order_by('id')
        context['date_of_birth'] = date(year=1996, month=5, day=18)
        context['age'] = 25 # переделать!!
        context['my_photo'] = 'ICY-mAf5sYY.jpg'
        context['stack'] = ('Python 3', 'Django', 'PostgreSQL', 'GIT', 'html, css (базовый уровень)', )
        return context

