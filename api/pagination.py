from rest_framework.pagination import PageNumberPagination


class BookPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_count'
    max_page_size = 100
