from project_manager.models import Task, Project
from datetime import datetime


def get_all_associated_tasks(project):
    """
    :param type project: Project "project object"
    :return:
    """
    return Task.objects.filter(project=project)


def create_new_project(name, members):
    """
    :type title: string
    :type members: list of [Member]
    :rtype: Project
    """
    project = Project(project_name=name, created_date=datetime.now())
    project.members.add(members)
    return project.save()
