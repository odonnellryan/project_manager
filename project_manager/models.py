from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=256)

    def __str__(self):
        return self.role_name


class Member(models.Model):
    member_name = models.CharField(max_length=256)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.member_name


class Project(models.Model):
    project_title = models.CharField(max_length=256)
    created_date = models.DateTimeField('date created')
    project_members = models.ManyToManyField(Member)

    def __str__(self):
        return self.project_title


class WorkItem(models.Model):
    item_title = models.CharField(max_length=256)
    item_description = models.CharField(max_length=5000)
    project = models.ForeignKey(Project)
    parent_item = models.ForeignKey('self')
    assigned_members = models.ManyToManyField(Member)

    def __str__(self):
        return self.item_title


class TimeEstimate(models.Model):
    member = models.ForeignKey(Member)
    work_item = models.ForeignKey(WorkItem)
    time = models.IntegerField()

    def __str__(self):
        return "_".join((self.member.member_name, self.work_item.item_title))
