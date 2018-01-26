from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20, null=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=20, null=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Bookmark(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=200,null=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
