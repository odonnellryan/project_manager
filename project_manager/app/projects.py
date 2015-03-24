from project_manager.models import Task, Project
from datetime import datetime


def get_tasks_by_project_pk(project_pk):
    """
    :param type project: Project "project object"
    :return:
    """
    project = Project.objects.get(pk=project_pk)
    return Task.objects.filter(project=project)


def create_new_project(name, members):
    """
    :type title: string
    :type members: list of [Member]
    :rtype: Project
    """
    project = Project(project_name=name, created_date=datetime.now())
    project.members.add(members)
    project.save()
    return project


def create_new_task(name, members, description, parent=None):
    """
    :type name: string
    :type members: list of [Member]
    :type description: string
    :type parent: Task
    :return:
    """
    task = Task(task_name=name, task_description=description, parent_item=parent)
    task.members.add(members)
    task.save()
    return task