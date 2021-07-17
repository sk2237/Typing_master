from django.db import models
from datetime import datetime,date


class Typing_practise(models.Model):
  user_id = models.IntegerField(blank=True)
  typing_speed = models.IntegerField()
  accuracy = models.IntegerField()
  post_date = models.DateField(auto_now_add = True)