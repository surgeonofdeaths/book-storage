from allauth.account.views import SignupView, LoginView
from django.urls import reverse_lazy

from common.utils import DataMixin


class CustomSignupView(DataMixin, SignupView):
    def get_context_data(self, **kwargs):
        new_context = {'title': 'Sign Up', 'selected': 'account_signup'}
        context = super().get_context_data(**new_context, **kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('view_profile', kwargs={'slug': self.request.POST.get('username')})


class CustomLoginView(DataMixin, LoginView):
    def get_context_data(self, **kwargs):
        new_context = {'title': 'Login', 'selected': 'account_login'}
        context = super().get_context_data(**new_context, **kwargs)
        return context
