from django.shortcuts import render
from project_manager.models import Task, Member, Project, TimeEstimate
from project_manager.app import  members, projects


def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project_manager/index.html', context)

def project(request, project_pk):
    tasks = projects.get_tasks_by_project_pk(project_pk)
    context = {'tasks': tasks}
    return render(request, 'project_manager/project.html', context)