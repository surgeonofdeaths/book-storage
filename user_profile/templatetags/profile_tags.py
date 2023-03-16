from django import template
from django.contrib.auth.models import User
from django.contrib.auth.views import get_user_model

from ..forms import ProfileForm, UserForm
from typing import Union

register = template.Library()


@register.inclusion_tag('profile/templatetags/profile_fields.html', name='get_profile_fields')
def generate_view_profile_fields(user: User):
    FIELDS = [
        {'name': 'Username', 'value': user.username},
        {'name': 'Email', 'value': user.email},
        {'name': 'First name', 'value': user.first_name},
        {'name': 'Last name', 'value': user.last_name},
        {'name': 'Sex', 'value': user.profile.gender},
        {'name': 'Bio', 'value': user.profile.bio},
    ]
    context = {'fields': FIELDS}
    return context


@register.inclusion_tag('profile/templatetags/iterate_profile_fields.html', name='generate_editable_profile_fields')
def iterate_profile_fields(form: Union[UserForm, ProfileForm]):
    return {'form': form}
