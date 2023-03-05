from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", CustomSignupView.as_view(), name="account_signup"),
    path("login/", CustomLoginView.as_view(), name="account_login"),
]
