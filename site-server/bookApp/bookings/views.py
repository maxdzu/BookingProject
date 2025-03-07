from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Accomodation, Spaces, Schedule, Booking
from .serializers import AccomodationSerializer, SpaceSerializer, ScheduleSerializer, BookingSerializer
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all(requset):
    accomodations = Accomodation.objects.all()
    serializer = AccomodationSerializer(accomodations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_spaces_by_accomodation(request, accomodation_id):
    try:
        accomodation = Accomodation.objects.get(id=accomodation_id)
    except Accomodation.DoesNotExist:
        return Response({"error": "Accomodation not found"}, status=404)

    spaces = Spaces.objects.filter(accomodation_id=accomodation_id)
    serializer = SpaceSerializer(spaces, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_schedule_for_accomodation(request, accomodation_id):
    try:
        accomodation = Accomodation.objects.get(id=accomodation_id)
    except Accomodation.DoesNotExist:
        return Response({"error": "Accomodation not found"}, status=404)

    schedules = Schedule.objects.filter(accomodation_id=accomodation_id)
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_booking(request):
    print("Request Data:", request.data)

    serializer = BookingSerializer(data=request.data)

    if not serializer.is_valid():
        print("Serializer Errors:", serializer.errors)
        return Response(serializer.errors, status=400)

    if serializer.is_valid():
        print("Serializer is valid:", serializer.validated_data)

        user = request.user
        start_time = serializer.validated_data['startTime']
        end_time = serializer.validated_data['endTime']
        accomodation = serializer.validated_data['accomodation']
        space = serializer.validated_data['space']

        date_only = start_time.date()
        if Schedule.objects.filter(accomodation=accomodation, day_off=date_only).exists():
            return Response({"error": "Accomodation is closed on this day"}, status=400)

        overlapping_bookings = Booking.objects.filter(
            space=space,
            status="confirmed",
            startTime__lt=end_time,
            endTime__gt=start_time
        )
        if overlapping_bookings.exists():
            return Response({"error": "This space is already booked for the selected time"}, status=400)

        booking = Booking.objects.create(
            user=user,
            startTime=start_time,
            endTime=end_time,
            accomodation=accomodation,
            space=space,
            orderTime=datetime.now(),
            status="pending"
        )

        return Response({"message": "Booking created successfully", "booking_id": booking.id}, status=201)

    return Response(serializer.errors, status=400)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_booking_time(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user != booking.user and not request.user.is_staff:
        return Response({"error": "You cannot change this reservation."}, status=403)

    new_start_time = request.data.get("startTime")
    new_end_time = request.data.get("endTime")

    if not new_start_time and not new_end_time:
        return Response({"error": "You must specify at least startTime or endTime"}, status=400)

    if new_start_time:
        try:
            new_start_time = datetime.fromisoformat(new_start_time)
        except ValueError:
            return Response({"error": "Incorrect format startTime"}, status=400)

    if new_end_time:
        try:
            new_end_time = datetime.fromisoformat(new_end_time)
        except ValueError:
            return Response({"error": "Incorrect format endTime"}, status=400)

    if new_start_time and new_end_time and new_start_time >= new_end_time:
        return Response({"error": "startTime should be earlier than endTime"}, status=400)

    if new_start_time:
        booking.startTime = new_start_time
    if new_end_time:
        booking.endTime = new_end_time

    booking.save()

    return Response({"message": "Booking time updated successfully"}, status=200)