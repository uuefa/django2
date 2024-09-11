from django.db import models

class Blog(models.Model):
  title = models.CharField(max_length=255)
  detail = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  dmy = models.IntegerField()