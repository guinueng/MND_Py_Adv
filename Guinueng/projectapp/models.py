from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='Project', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    description = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'
