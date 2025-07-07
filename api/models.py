from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)  # email & password inherited from the AbstractUser

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.number}"

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Resv {self.id} by {self.user.username}"

class Payment(models.Model):
    METHOD_CHOICES = [
        ('cash',       'Cash'),
        ('electronic', 'Electronic'),
    ]

    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    method=models.CharField(max_length=10, choices=METHOD_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} for Resv {self.reservation.id}"

class Invoice(models.Model):
    reservation  = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id}"

class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    discount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Offer {self.title}"


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('open',     'Open'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
        ('escalated','Escalated'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint {self.id}"

class Response(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='responses')
    responder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # an employee
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response {self.id} to Complaint {self.complaint.id}"


class Report(models.Model):
    date = models.DateField(auto_now_add=True)
    content=models.TextField()

    def __str__(self):
        return f"Report {self.id} on {self.date}"

