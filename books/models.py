from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.title
