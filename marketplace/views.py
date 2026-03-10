from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product
from .permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from .pagination import ProductPagination

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

    # Farmer dashboard = GET /products/my_products/
    @action(detail=False, methods=['get'])
    def my_products(self, request):
        products = Product.objects.filter(farmer=request.user)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    #request.user=logged-in user
    #serializer.save(farmer=request.user)=assigns owner to product
    #Customer.objects.get(user=request.user)=get user's profile model