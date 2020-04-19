from django.urls import path
from actstream.feeds import CustomJSONActivityFeed

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stream/', views.stream, name='stream'),
    path('stream/<content_type_id>', views.model, name='stream_model'),
    path('feeds/mystream/', CustomJSONActivityFeed.as_view(), name='feed')

]


