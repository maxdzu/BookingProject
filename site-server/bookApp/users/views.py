from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, UserSerializer
from django.contrib.auth import login
from django.contrib.auth.models import update_last_login
from bookings.models import Booking
from bookings.serializers import BookingSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User created successfully'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user:
            update_last_login(None, user)
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
        return Response({'error': 'Incorrect credentials'}, status=401)

    return Response(serializer.errors, status=400)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        user = request.user
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']

        if not check_password(old_password, user.password):
            return Response({'error': 'Incorrect old password'}, status=400)

        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password changed successfully'}, status=200)

    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_bookings(request):
    user = request.user
    bookings = Booking.objects.filter(user_id=user.id)
    serializer = BookingSerializer(bookings, many=True)

    return Response(serializer.data if serializer.data else {"message": "You haven`t any bookings yet"})

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user != booking.user and not request.user.is_staff:
        return Response({"error": "You do not have permission to cancel this booking"}, status=403)

    booking.status = "cancelled"
    booking.save()

    return Response({"message": "Booking cancelled successfully", "booking_id": booking.id}, status=200)
