from django.db import models

# Create your models here.

class TaskManager(models.Manager):
  def get_by_id(self, id):
    qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
    if qs.count() == 1:
      return qs.first()
    return None


class Task(models.Model):
  task  = models.CharField(max_length=100)

  objects = TaskManager()

  def get_absolute_url(self):
    return "{pk}/".format(pk=self.pk)

  def str(self):
    return self.task