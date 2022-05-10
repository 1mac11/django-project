from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views import RegisterView, LogoutView, UserViewSet, AccessTokenView

app_name = 'accounts'
router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register-user'),
    path('token/', AccessTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Uncomment if you want to check token to HMAC
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('logout/', LogoutView.as_view(), name='register-user'),

]
urlpatterns += router.urls
