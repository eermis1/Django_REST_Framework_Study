from rest_framework.pagination import PageNumberPagination


class Community_Pagination(PageNumberPagination):
    page_size=5


class Post_Pagination(PageNumberPagination):
    page_size=5


class Comment_Pagination(PageNumberPagination):
    page_size=5