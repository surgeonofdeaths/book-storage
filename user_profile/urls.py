from django.urls import path

from .views import ProfileDetailView, ProfileEditView

urlpatterns = [
    path('view/<slug:slug>/', ProfileDetailView.as_view(), name='view_profile'),
    path('edit/<slug:slug>/', ProfileEditView.as_view(), name='edit_profile'),
]
