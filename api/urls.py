from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# from .views import BookViewSet
from .views import BookAPIList, BookAPIUpdate

# router = routers.DefaultRouter()
# router.register('books', BookViewSet, basename='book')
# router = routers.DefaultRouter()
# router.register('books', BookViewSet, basename='book')
# print(router.urls)

# urlpatterns = router.urls

urlpatterns = [
    path('books/', BookAPIList.as_view(), name='book-list'),
    path('books/<slug:slug>/', BookAPIUpdate.as_view(), name='book-detail'),
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
