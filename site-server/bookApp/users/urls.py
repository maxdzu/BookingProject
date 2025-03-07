from django.urls import path
from .views import register_user, login_user, change_password, get_user, get_user_bookings, cancel_booking
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('change-password/', change_password, name='change_password'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', get_user, name='user_profile'),
    path('user-bookings/', get_user_bookings, name='user_bookings'),
    path('user-bookings/<int:booking_id>/cancel/', cancel_booking, name='cancel-booking')
]