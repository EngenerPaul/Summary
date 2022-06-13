from django.contrib import admin

from .models import Course, PetProject, TechnologyStack

admin.site.register(Course)
admin.site.register(PetProject)
admin.site.register(TechnologyStack)
