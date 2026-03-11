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
    def validate(self, attrs):

        product = attrs.get("product")
        quantity = attrs.get("quantity")
        request = self.context.get("request")

        if request and product.farmer == request.user:
            raise serializers.ValidationError(
                "You cannot order your own product."
            )

        if quantity > product.stock:
            raise serializers.ValidationError(
                "Not enough stock available."
            )

        return attrs

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    class Meta :
        model = Order
        fields = ['id','user','payment_status' ,'payment_method','delivery_address','created_at', 'updated_at','items' ]
        read_only_fields = ['id' , 'user' ,'created_at', 'updated_at']

    #def validate_user(self , value)    
                
