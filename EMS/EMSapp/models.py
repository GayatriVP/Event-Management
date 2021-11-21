from django.db import models

# Create your models here.


class Customers(models.Model):
    cust_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)


class Bookings(models.Model):
    book_id = models.AutoField(primary_key=True)
    slots = models.CharField(max_length=150)
    event_type = models.CharField(max_length=150)
    capacity = models.CharField(max_length=50)
    services = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    customer_id = models.ForeignKey(
        'EMSapp.Customers', on_delete=models.CASCADE, null=True)
    cust_event_id = models.ForeignKey(
        'EMSapp.Events', on_delete=models.CASCADE, null=True)


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=150)
    av_slots = models.CharField(max_length=150)
    cap = models.CharField(max_length=150, default="")
    serv = models.CharField(max_length=150, default="")
