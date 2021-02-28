from django.db import models

# Create your models here.
class babySitter(models.Model):
    name = models.TextField(max_length=200)
    email = models.EmailField(max_length=254)
    msg = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
