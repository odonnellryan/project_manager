from django.contrib import admin
from project_manager.models import Member, Project, Task, TimeEstimate, Role

admin.site.register((Member, Project, Task, TimeEstimate, Role))

# Register your models here.
