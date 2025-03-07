from django.urls import path
from .views import send_booking_confirmation_email, confirm_booking

urlpatterns = [
    path("send-confirmation/<int:booking_id>/", send_booking_confirmation_email, name="send-confirmation"),
    path("confirm/<int:booking_id>/", confirm_booking, name="confirm-booking"),
]