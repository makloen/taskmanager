from django.db import models

# Create your models here.

class Task(models.Model):
  task  = models.CharField(max_length=100)

  def get_absolute_url(self):
    return "{pk}/".format(pk=self.pk)

  def str(self):
    return self.task