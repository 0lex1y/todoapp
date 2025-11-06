from django import forms
from django.views import generic

from task.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'deadline', 'tags']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'datetime-local'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'size': 5}),
        }