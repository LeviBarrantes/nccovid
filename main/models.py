from django.db import models


class Record(models.Model):

    # Building a record
    country = models.TextField()
    state = models.CharField(max_length=2)
    city = models.TextField()
    date = models.DateTimeField()


class Outcome(models.Model):

    # Outcome values
    recovered = models.BooleanField()
    death = models.BooleanField()