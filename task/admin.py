from django.contrib import admin

from task.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "deadline", "complete")
    search_fields = ("title",)
    list_filter = ("deadline", "complete")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

