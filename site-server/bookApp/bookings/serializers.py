from rest_framework import serializers
from .models import Booking, Accomodation, Spaces, Schedule


class BookingSerializer(serializers.ModelSerializer):
    startTime = serializers.DateTimeField(
        format='%Y-%m-%dT%H:%M:%S',
        input_formats=['%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%SZ']
    )
    endTime = serializers.DateTimeField(
        format='%Y-%m-%dT%H:%M:%S',
        input_formats=['%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%SZ']
    )

    accomodation_id = serializers.PrimaryKeyRelatedField(
        queryset=Accomodation.objects.all(),
        source='accomodation',  # Указываем связь с моделью
        write_only=True
    )
    space_id = serializers.PrimaryKeyRelatedField(
        queryset=Spaces.objects.all(),
        source='space',
        write_only=True
    )

    class Meta:
        model = Booking
        fields = ['id', 'startTime', 'endTime', 'accomodation_id', 'space_id']


class AccomodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accomodation
        fields = ['id', 'title', 'rating', 'description']


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spaces
        fields = ['id', 'name', 'capacity']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'accomodation_id', 'day_off']