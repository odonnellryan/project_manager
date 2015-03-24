from django import forms

class ProjectForm(forms.Form):
    project_title = forms.CharField(label='Your name', max_length=100)
    project_members = forms.CharField