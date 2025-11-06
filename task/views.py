from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskForm
from task.models import Task, Tag


class TasksListView(generic.ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task_list.html'

def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = not task.complete
    task.save()
    return redirect(reverse_lazy('task:tasks_list'))

class TasksCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:tasks_list')

class TasksUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('task:tasks_list')


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'task/tags_list.html'

class TagsCreateView(generic.CreateView):
    model = Tag
    fields = '__all__'
    template_name = 'task/tag_form.html'
    success_url = reverse_lazy('task:tags_list')

class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('task:tags_list')

class TagsDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'task/tag_delete_confirm.html'
    success_url = reverse_lazy('task:tags_list')