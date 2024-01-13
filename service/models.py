from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to="service/images/")