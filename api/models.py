from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20)
    priority = models.IntegerField(blank=False, null=False)
    limit = models.DateTimeField(help_text="期限")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title