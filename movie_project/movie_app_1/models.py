from django.db import models


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='dynamic')

    def __str__(self):
        return self.title