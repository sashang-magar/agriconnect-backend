from rest_framework import serializers
from .models import Product , Order ,OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id' ,'name' ,'unit' , 'quantity' , 'unit_price' ,'category' , 'district','image' , 'harvest_date']
        read_only_fields = ['id','farmer']


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name' , 'unit_price']

class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta:
        model = OrderItem
        fields = [ 'id' ,'product' , 'quantity' , 'unit_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta :
        model = Order
        fields = ['id','user','payment_status' ,'payment_method','delivery_address','created_at', 'updated_at','items' ]
        read_only_fields = ['id' , 'user' ,'created_at', 'updated_at']
                
