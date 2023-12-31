from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo_url = models.URLField()

    def __str__(self):
        return self.title
