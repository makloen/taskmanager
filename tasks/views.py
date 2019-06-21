from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import AddTaskForm

# Create your views here.


class TaskListView(ListView):
	queryset = Task.objects.all()
	template_name = 'list_view.html'



def detail_view(request, pk=None, *args, **kwargs):
  instance = get_object_or_404(Task, pk=pk)
  form = AddTaskForm(request.POST or None, request.FILES or None, instance=instance)

  if form.is_valid():
    if 'savebutton' in request.POST:
      instance = form.save(commit=False)
      instance.save()
      return redirect("list")

    elif 'deletebutton' in request.POST:
      instance.delete()
      return redirect("list")

  context = {
    'object': instance,
    'form': form
  }

  return render(request, 'detail_view.html', context)




def add_view(request):
  form = AddTaskForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    return redirect("list")

  context = {
    'form': form
  }
  return render(request, 'add_view.html', context)