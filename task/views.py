from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import RedirectView

from task.forms import TaskForm
from task.models import Task, Tag


class TasksListView(generic.ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task_list.html'

class ToggleTaskCompleteView(RedirectView):
    pattern_name = 'task:tasks_list'

    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        task.complete = not task.complete
        task.save()
        return super().get_redirect_url(*args, **kwargs)


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