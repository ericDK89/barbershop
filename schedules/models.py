from django.db import models
from django.contrib.auth.models import User

class Schedules(models.Model):
  hair = models.BooleanField(default=False)
  eyebrow = models.BooleanField(default=False)
  beard = models.BooleanField(default=False)
  date = models.DateField()
  time = models.CharField(max_length=255)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  price = models.IntegerField()
  
  def __str__(self) -> str:
    return f'{self.user}' 