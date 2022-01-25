from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'summary/index.html'
    context = {
        'my_photo': 'ICY-mAf5sYY.jpg',
    }
    return render(request, template_name=template, context=context)
