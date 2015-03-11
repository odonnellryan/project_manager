from django.contrib import admin
from project_manager.models import Member, Project, WorkItem, TimeEstimate, Role

admin.site.register((Member, Project, WorkItem, TimeEstimate, Role))

# Register your models here.
