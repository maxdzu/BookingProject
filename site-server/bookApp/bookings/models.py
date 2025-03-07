from django.db import models
from users.models import User

class Accomodation(models.Model):
    title = models.CharField(max_length=256)
    rating = models.IntegerField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Schedule(models.Model):
    accomodation = models.ForeignKey(to=Accomodation, on_delete=models.CASCADE)
    day_off = models.DateField()

    def __str__(self):
        return f"{self.accomodation.title} closed on {self.day_off}"


class Spaces(models.Model):
    accomodation = models.ForeignKey(to=Accomodation, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.accomodation.title})"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ]

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    space = models.ForeignKey(to=Spaces, on_delete=models.CASCADE)
    accomodation = models.ForeignKey(to=Accomodation, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    orderTime = models.DateTimeField(auto_now_add=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    def __str__(self):
        return f"Booking by {self.user.username} for {self.space.name} on {self.start_time}"