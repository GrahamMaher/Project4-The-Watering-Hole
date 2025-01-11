from django.db import models

# Create your models here.
class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()

    def __str__(self):
        return f'Table {self.number} - Seats: {self.seats}'


class Reservation(models.Models):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date_time = models.DateTimeField()
    guests = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return f'Reservation for {self.name} on {self.date_time}'