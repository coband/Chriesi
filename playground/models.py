from django.db import models

class Book(models.Model):
    Titel = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    ISBN = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
  

    def __str__(self):
        return self.title

