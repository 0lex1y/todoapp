from django.urls import path
from .views import (TasksListView,
                    TasksCreateView,
                    TasksUpdateView,
                    TagsListView,
                    TagsCreateView,
                    TagsUpdateView,
                    TagsDeleteView,
                    ToggleTaskCompleteView,)


app_name = 'task'


urlpatterns = [
    path('', TasksListView.as_view(), name='tasks_list'),
    path('task/<int:pk>/toggle/', ToggleTaskCompleteView.as_view(), name='tasks_toggle'),
    path('task/create/', TasksCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TasksUpdateView.as_view(), name='task_update'),
    path('tags/', TagsListView.as_view(), name='tags_list'),
    path('tags/create/', TagsCreateView.as_view(), name='tags_create'),
    path('tags/<int:pk>/update/', TagsUpdateView.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete/', TagsDeleteView.as_view(), name='tags_delete'),
]
