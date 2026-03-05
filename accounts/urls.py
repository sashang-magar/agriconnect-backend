from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, LoginView, FarmerProfileViewSet,BuyerProfileViewSet

#for ModelViewSet
# router = DefaultRouter()
# router.register('farmer/profile/', FarmerProfileViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("farmer/profile/", FarmerProfileViewSet.as_view()),
    path("buyer/profile/", BuyerProfileViewSet.as_view()),

    #modelViewSet
    # path('', include(router.urls)),
]