from django.db import models

# Create your models here.
class Typing_practise(models.Model):
  user_id = models.IntegerField(blank=True)
  typing_speed = models.IntegerField()
  accuracy = models.IntegerField()
