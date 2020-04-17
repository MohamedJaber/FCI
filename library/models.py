from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=30)
    day = models.CharField(default='Sunday', max_length=20)
    subject = models.CharField(max_length=30)
    place = models.CharField(default='Place 1', max_length=20)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return self.subject


class Contact(models.Model):
    name1 = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name1


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.username
