from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Book


class BookPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user == Book.objects.get(slug=self.kwargs.get('slug')).user
