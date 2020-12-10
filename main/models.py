from django.db import models


# Create Sheets for Local News Links #


class NYTimes(models.Model):
    article_title = models.TextField()


class USAToday(models.Model):
    article_title = models.TextField()


class WRAL(models.Model):
    article_title = models.TextField()


class WCNC(models.Model):
    article_title = models.TextField()


class WCCB(models.Model):
    article_title = models.TextField()
