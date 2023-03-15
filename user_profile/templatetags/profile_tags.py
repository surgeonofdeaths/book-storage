from django import template
from django.contrib.auth.models import User
from django.contrib.auth.views import get_user_model

register = template.Library()


@register.inclusion_tag('profile/templatetags/profile_fields.html', name='fields')
def profile_fields(user: User):
    FIELDS = [
        {'name': 'Username', 'command': user.username},
        {'name': 'Email', 'command': user.email},
        {'name': 'First name', 'command': user.first_name},
        {'name': 'Last name', 'command': user.last_name},
        {'name': 'Sex', 'command': user.profile.gender},
        {'name': 'Bio', 'command': user.profile.bio},
    ]
    context = {'fields': FIELDS}
    return context

