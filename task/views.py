from django.views import generic

from task.models import Task, Tag


class TasksListView(generic.ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'tasks/tags_list.html'