from django.urls import reverse
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages

from common.utils import DataMixin
from .forms import ProfileForm, UserForm

User = get_user_model()


class ProfileDetailView(DataMixin, LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'shown_user'
    template_name = 'profile/view_profile.html'

    def get_context_data(self, **kwargs):
        new_context = {'title': f'Profile: {self.request.user.username}'}
        return super().get_context_data(**new_context, **kwargs)


class ProfileEditView(DataMixin, LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'profile/edit_profile.html'

    def get_context_data(self, slug, **kwargs):
        new_context = kwargs
        new_context.setdefault('title', f'Profile: {self.request.user.username}')
        new_context.setdefault('profile_form', ProfileForm(self.request.FILES, instance=self.request.user.profile))
        new_context.setdefault('user_form', UserForm(instance=self.request.user))
        context = super().get_context_data(**new_context)
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(**kwargs))

    def post(self, request, slug, *args, **kwargs):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Your profile has been successfully updated!')
            return redirect(reverse('view_profile', kwargs={'slug': slug}))
        messages.error(request, "Couldn't save your profile.")
        new_context = {'profile_form': profile_form, 'user_form': user_form}
        return render(request, self.template_name, self.get_context_data(slug, **new_context))

    def test_func(self):
        return self.request.user.slug == self.kwargs.get('slug')
