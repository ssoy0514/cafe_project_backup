from rest_framework import serializers
from .models import Menu, Category, Event, Carosel, Home, Order, Coupon

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        
class CaroselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carosel
        fields = "__all__"
class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"