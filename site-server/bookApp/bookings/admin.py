from django.contrib import admin

# Register your models here.
from bookings.models import Accomodation, Schedule, Spaces, Booking

admin.site.register(Accomodation)
admin.site.register(Schedule)
admin.site.register(Spaces)
admin.site.register(Booking)