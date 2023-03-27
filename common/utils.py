from copy import deepcopy


header_menu = [
    {'title': 'Home', 'url': 'home', 'selected': 0},
    {'title': 'About', 'url': 'about', 'selected': 0},
    {'title': 'Books', 'url': 'books', 'selected': 0},
    {'title': 'Publish Book', 'url': 'publish_book', 'selected': 0},
]


class _FetchData:
    def get_common_context(self, **kwargs):
        context = kwargs
        context['selected'] = context.get('selected', None)
        header_menu_copy = deepcopy(header_menu)
        if self.request.user.is_authenticated:
            header_menu_copy.append({'title': 'Logout', 'url': 'account_logout', 'selected': 0})
        else:
            header_menu_copy.extend([
                {'title': 'Login', 'url': 'account_login', 'selected': 0},
                {'title': 'Sign Up', 'url': 'account_signup', 'selected': 0},
            ])
        for menu_item in header_menu_copy:
            if menu_item['url'] == context['selected']:
                menu_item['selected'] = 1
                break
        context['header_menu'] = header_menu_copy
        return context


class DataMixin(_FetchData):
    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except AttributeError:
            context = kwargs
        common_context = self.get_common_context(**context)
        context.update(common_context)
        return context
