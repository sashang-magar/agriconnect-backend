from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer, ProductSerializer , UpdateOrderSerializer ,CreateOrderSerializer
from .models import Order, Product
from .permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination, Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from .pagination import ProductPagination
from rest_framework import status

class ProductViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #overriding globally set 10 to 5 per page 
    pagination_class = ProductPagination
    #filtering and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category' , 'district'] #DjangoFilterBackend
    search_fields = ['name'] #SearchFilter
    ordering_fields = ['name' , 'harvest_date' , 'unit_price'] #OrderingFilter


    #automatically assign the logged-in user as the farmer
    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user)

    # Farmer dashboard = GET /products/my_products/ @action used for extra endpoints
    @action(detail=False, methods=['get'])
    def my_products(self, request):
        products = Product.objects.filter(farmer=request.user)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    #request.user=logged-in user
    #serializer.save(farmer=request.user)=assigns owner to product
    #Customer.objects.get(user=request.user)=get user's profile model

class OrderViewSet(ModelViewSet):
    #permission_classes =[]
    queryset = Order.objects.all() 
    serializer_class = OrderSerializer   

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateOrderSerializer

        if self.action in ['update', 'partial_update']:
            return UpdateOrderSerializer

        return OrderSerializer
    
    @action(detail=False , methods=['get'])
    def my_order(self , request):
        if request.user != 'BUYER':
            return Response({'error':'Only buyer can access their product'} , status=status.HTTP_403_FORBIDDEN)
        
        orders = Order.objects.filter(user = request.user).prefetch_related('items', 'items__product', 'items__product__farmer')
        serializer = OrderSerializer(orders ,many = True )
        return Response(serializer.data)

    @action(detail=False , methods=['get'])
    def incoming_order(self , request):
        if request.user != ['FARMER']:
            return Response({'error':'Only farmers can access incoming orders'} , status=status.HTTP_403_FORBIDDEN)

        orders = Order.objects.filter(user  =request.user).prefetch_related( 
            'items', 
            'items__product', 
            'items__product__farmer',
            'user'
            )
        serializer = OrderSerializer(orders , many = True)
        return Response(serializer.data)
