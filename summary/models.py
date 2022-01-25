from django.db import models
from django.forms import CharField, ImageField, Textarea

# Create your models here.

# class Course(models.Model):
#     site_name = CharField(max_length=30, blank=True) # path of homepage of the site
#     site_link = CharField(max_length=25, blank=True) # link to site homepage
    # course_title = CharField(max_length=100) 
#     course_link = CharField(max_length=100, blank=True) # path to the course
#     certificate = ImageField(upload_to='certificates/', blank=True)


# class PetProject(models.Model):
#     # site_title = CharField(max_length=100) # name of site
#     # use re!!
#     site_link = CharField(max_length=50) # path of homepage of the site 
#     note = Textarea(blank=True) # how the site works
    # homepage_photo = ImageField(upload_to='pet-projects', blank=True)
    # git_repository = CharField(max_length=50, blank=True)