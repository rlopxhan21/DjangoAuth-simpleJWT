from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from .views import RegisterationView, MyTokenObtainPairView, ProfileDataView, SingleProfileDataView, BasicInfoChangeView, PasswordChangeView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name="login"),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    path('register/', RegisterationView.as_view(), name="register" ),

    path('blacklist/', TokenBlacklistView.as_view(), name="token_blacklist"),

    path('users/', ProfileDataView.as_view(), name="proile_data"),
    path('users/<int:pk>/', SingleProfileDataView.as_view(), name="sinleprofile_data"),
    path('users/<int:pk>/update/', BasicInfoChangeView.as_view(), name="basic_info_change"),
    path('users/<int:pk>/passupdate/', PasswordChangeView.as_view(), name="password_change"),


]
