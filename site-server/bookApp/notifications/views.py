from django.contrib.sites import requests
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

BOOKINGS_SERVICE_URL = "http://127.0.0.1:8000/a/bookings"


def send_booking_confirmation_email(request, booking_id):

    user_email = request.user.email
    confirmation_url = f"http://127.0.0.1:8000/a/notifications/confirm/{booking_id}/"

    subject = "Booking confirmation"
    message = f"""
    Greetings!

    You have created a booking. Confirm it using the link:

    <a href="{confirmation_url}">Confirm booking</a>

    Thanks for your attention, we appreciate that you are using our service!
    """

    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email], html_message=message)

    return JsonResponse({"message": "Email sent"}, status=200)


@csrf_exempt
def confirm_booking(request, booking_id):
    try:
        response = requests.patch(f"{BOOKINGS_SERVICE_URL}/{booking_id}/", json={"status": "confirmed"})

        if response.status_code == 200:
            return JsonResponse({"message": "Booking confirmed!"}, status=200)
        else:
            return JsonResponse({"error": "Failed to update booking status"}, status=response.status_code)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)