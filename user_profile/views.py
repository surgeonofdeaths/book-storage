from django.views.generic import DetailView, FormView
from django.contrib.auth.views import get_user_model
from django.shortcuts import get_object_or_404

from common.utils import DataMixin

User = get_user_model()


class ProfileDetailView(DataMixin, FormView):
    form_classes = [User]
    template_name = 'profile/view_profile.html'
    context_object_name = 'user_profile'

    def get_context_data(self, **kwargs):
        show_user = User.objects.get(slug=self.kwargs['slug'])
        # show_user = get_object_or_404(User, slug=self.request.GET.get('slug'))
        new_content = {'title': f'{self.request.user.username[:25]}', 'show_user': show_user}
        context = super().get_context_data(**new_content, **kwargs)
        return context


# class ProfileDetailView(DataMixin, DetailView):
#     model = User
#     template_name = 'profile/view_profile.html'
#     context_object_name = 'user_profile'
#
#     def get_context_data(self, **kwargs):
#         show_user = User.objects.get(slug=self.kwargs['slug'])
#         # show_user = get_object_or_404(User, slug=self.request.GET.get('slug'))
#         new_content = {'title': f'{self.request.user.username[:25]}', 'show_user': show_user}
#         context = super().get_context_data(**new_content, **kwargs)
#         return context



