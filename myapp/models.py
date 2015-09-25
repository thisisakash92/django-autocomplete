from django.db import models

# Create your models here.

class SampleModel(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

    def get_absolute_url(self):
        return "https://www.google.co.in/?q="+self.name