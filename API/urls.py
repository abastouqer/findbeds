from .routers import router
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from auth1.views import MyObtainTokenPairView
urlpatterns = [
    path('', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls