from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/users/', include('users.urls')),
    path('a/bookings/', include('bookings.urls')),
    path('a/notifications/', include('notifications.urls')),
]