from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=256)


class Member(models.Model):
    member_name = models.CharField(max_length=256)
    roles = models.ManyToManyField(Role)


class Project(models.Model):
    project_title = models.CharField(max_length=256)
    created_date = models.DateTimeField('date created')
    project_members = models.ManyToManyField(Member)

class WorkItem(models.Model):
    item_title = models.CharField(max_length=256)
    item_description = models.CharField(max_length=5000)
    project = models.ForeignKey(Project)
    parent_item = models.ForeignKey('self')
    assigned_members = models.ManyToManyField(Member)

class TimeEstimate(models.Model):
    member = models.ForeignKey(Member)
    work_item = models.ForeignKey(WorkItem)
    time = models.IntegerField()



