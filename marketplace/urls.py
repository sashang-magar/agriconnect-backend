from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet ,OrderViewSet

#for ModelViewSet
router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('orders' ,OrderViewSet , basename='order')

urlpatterns = router.urls