from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Menu, Category, Event,Home, Carosel, Coupon, Order
from .serializers import (
    MenuSerializer,
    CategorySerializer,
    EventSerializer,
    CaroselSerializer,
    OrderSerializer,
    HomeSerializer,
    CouponSerializer
)

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class CaroselViewSet(viewsets.ModelViewSet):
    queryset = Carosel.objects.all()
    serializer_class = CaroselSerializer
    
class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
