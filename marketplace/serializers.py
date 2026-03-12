from rest_framework import serializers
from .models import Product , Order ,OrderItem
from django.db import transaction

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
    product = SimpleProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField() #total_price is not stored in the database
    class Meta:
        model = OrderItem
        fields = [ 'id' ,'product' , 'quantity' , 'unit_price','total_price']

    def get_total_price(self , order_item:OrderItem):
        return order_item.quantity * order_item.unit_price    

    # def validate_quantity(self , value):
    #     if value <= 0 :
    #         raise serializers.ValidationError('Quantity must be greater than zero.')  
    #     return value


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    class Meta :
        model = Order
        fields = ['id','user','payment_status' ,'payment_method','delivery_address','created_at', 'updated_at','items' ]
        read_only_fields = ['id' , 'user' ,'created_at', 'updated_at']

 
class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']     

class CreateOrderSerializer(serializers.Serializer):      
        items = serializers.ListField()
        delivery_address = serializers.CharField()
        payment_method = serializers.CharField()

        def validate(self, attrs):
            items = attrs.get('items')
            if not items:
                raise serializers.ValidationError('Must contain atleast one product')
            
            return attrs
        
        def create(self, validated_data):
            items_data = validated_data["items"]
            delivery_address = validated_data["delivery_address"]
            payment_method = validated_data["payment_method"]

            user = self.context["request"].user

            with transaction.atomic():
                order = Order.objects.create(
                    user = user,
                    delivery_address=delivery_address,
                    payment_method = payment_method
                )

                for item in items_data:
                    product =Product.objects.get(id=item['product']) 
                    quantity = item['quantity']

                    if quantity > product.stock:
                        raise serializers.ValidationError('Not enough stock available.')
                    
                    if product.farmer == user:
                        raise serializers.ValidationError('Cannot order own product')
                    
                    OrderItem.objects.create(
                        order = order,
                        product = product,
                        quantity = quantity,
                        unit_price = product.unit_price
                    )

                    product.stock -= quantity
                    product.save()

            return order
