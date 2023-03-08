from django.urls import path

from .views import ProfileDetailView

urlpatterns = [
    path('view/<slug:slug>/', ProfileDetailView.as_view(), name='view_profile')
]
