from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=100, unique=True)
    mobile = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
