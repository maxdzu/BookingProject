from django.urls import path
from .views import (get_all, get_spaces_by_accomodation, get_schedule_for_accomodation,
                    create_booking, update_booking_time)

urlpatterns = [
    path('accomodations/', get_all, name='all_accomodations'),
    path('accomodations/<int:accomodation_id>/spaces/', get_spaces_by_accomodation, name='spaces_by_accomodation'),
    path('accomodations/<int:accomodation_id>/schedules/', get_schedule_for_accomodation, name='schedule_for_accomodation'),
    path('create/', create_booking, name='create_booking'),
    path("<int:booking_id>/update-time/", update_booking_time, name="update-booking-time")
]