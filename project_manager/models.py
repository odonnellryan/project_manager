from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.role_name


class Member(models.Model):
    member_name = models.CharField(max_length=256, null=False)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.member_name


class Project(models.Model):
    project_name = models.CharField(max_length=256, null=False)
    created_date = models.DateTimeField('date created', null=False)
    project_members = models.ManyToManyField(Member)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    task_name = models.CharField(max_length=256, null=False)
    task_description = models.CharField(max_length=5000, null=False)
    project = models.ForeignKey(Project)
    parent_item = models.ForeignKey('self')
    assigned_members = models.ManyToManyField(Member)

    def __str__(self):
        return self.task_name


class TimeEstimate(models.Model):
    member = models.ForeignKey(Member)
    task = models.ForeignKey(Task)
    time = models.IntegerField(null=False)

    def __str__(self):
        return "_".join((self.member.member_name, self.task.task_name))
