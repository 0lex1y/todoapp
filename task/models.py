from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", blank=True, related_name="tasks")

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=255)

