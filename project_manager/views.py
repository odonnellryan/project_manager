from django.shortcuts import render
from project_manager.models import Task, Member, Project, TimeEstimate

def index(request):
    tasks = Project.objects.order_by
    return render(context)