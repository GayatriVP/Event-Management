from django.contrib import admin

# Register your models here.
from .models import Customers, Bookings, Events


admin.site.register(Customers)
admin.site.register(Bookings)
admin.site.register(Events)
