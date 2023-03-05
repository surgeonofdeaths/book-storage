from allauth.account.views import SignupView, LoginView

from common.utils import DataMixin


class CustomSignupView(DataMixin, SignupView):
    def get_context_data(self, **kwargs):
        new_context = {'title': 'Sign Up', 'selected': 'account_signup'}
        context = super().get_context_data(**new_context, **kwargs)
        return context


class CustomLoginView(DataMixin, LoginView):
    def get_context_data(self, **kwargs):
        new_context = {'title': 'Login', 'selected': 'account_login'}
        context = super().get_context_data(**new_context, **kwargs)
        return context
