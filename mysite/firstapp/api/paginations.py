from rest_framework.pagination import PageNumberPagination


class Community_Pagination(PageNumberPagination):
    page_size=5