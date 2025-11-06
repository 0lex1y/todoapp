from django.urls import path
from .views import TasksListView, TagsListView


app_name = 'task'


urlpatterns = [
    path('', TasksListView.as_view(), name='tasks_list'),
    path('tags/', TagsListView.as_view(), name='tags_list'),
]
