from django.db import models
from django.db.models import CharField, ImageField, TextField

# Create your models here.

class Course(models.Model):
    site_name = CharField(max_length=30, blank=True, verbose_name='Название сайта') # path of homepage of the site
    site_link = CharField(max_length=50, blank=True, verbose_name='Ссылка на сайт') # link to site homepage
    course_title = CharField(max_length=100, verbose_name='Название курса') 
    course_link = CharField(max_length=100, blank=True, verbose_name='Ссылка на курс') # path to the course
    certificate = ImageField(upload_to='certificates/', blank=True, verbose_name='Сертификат')
# сертификат будет отображаться на отдельной странице (по ссылке)

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

class PetProject(models.Model):
    site_title = CharField(max_length=100, verbose_name='Название сайта') # site about..
    site_link = CharField(max_length=50, verbose_name='Ссылка на сайт') # path of homepage of a site 
    site_description = CharField(max_length=100, verbose_name='Краткое описание') # briefly decription of a site
    note = TextField(blank=True, verbose_name='Описание сайта') # how the site works
    homepage_photo = ImageField(upload_to='pet-projects/', blank=True, verbose_name='Фотка главной сайта')
    git_repository = CharField(max_length=50, blank=True, verbose_name='GitHub')

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = 'Pet-project'
        verbose_name_plural = 'Pet-projects'