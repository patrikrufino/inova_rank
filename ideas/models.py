from django.db import models

# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField()
    num_genius = models.BigIntegerField(default=0)
    num_stupid = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
