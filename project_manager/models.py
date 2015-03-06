from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=256)

class Member(models.Model):
    member_name = models.CharField(max_length=256)
    roles = models.ManyToManyField(Role)

class Project(models.Model):
    project_name = models.CharField(max_length=256)
    created_date = models.DateTimeField('date created')
    project_members = models.ManyToManyField(Member)

class WorkItem(models.Model):
    project = models.ForeignKey(Project)
