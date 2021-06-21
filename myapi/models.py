from django.db import models

# Create your models here.

class Input(models.Model):
     name = models.CharField(max_length=150)
     message = models.CharField(max_length=500)

     def _str_(self):
          return self.name
