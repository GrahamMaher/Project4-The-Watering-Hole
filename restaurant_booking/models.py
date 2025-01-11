from django.db import models

# Create your models here.
class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()


class Reservation(models.Models):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date_time = models.DateTimeField()
    guests = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)