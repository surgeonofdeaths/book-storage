from django.urls import path
from rest_framework import routers

# from .views import BookViewSet
from .views import BookAPIList, BookAPIUpdate, BookAPIDestroy

# router = routers.DefaultRouter()
# router.register('books', BookViewSet, basename='book')
# router = routers.DefaultRouter()
# router.register('books', BookViewSet, basename='book')
# print(router.urls)

# urlpatterns = router.urls

urlpatterns = [
    path('books/', BookAPIList.as_view(), name='book-list'),
    path('books/<slug:slug>/', BookAPIUpdate.as_view(), name='book-update'),
    path('books/delete/<slug:slug>/', BookAPIDestroy.as_view(), name='book-destroy'),
]
