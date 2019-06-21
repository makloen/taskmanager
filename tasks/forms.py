from django import forms
from .models import Task


class AddTaskForm(forms.ModelForm):
  task = forms.CharField(
    label='',
    widget=forms.TextInput(attrs={"placeholder":"New task", "class":"form-control my-1"})
  )

  class Meta:
    model = Task
    fields = ["task"]