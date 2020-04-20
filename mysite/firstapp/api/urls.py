from django.urls import path
from actstream.feeds import CustomJSONActivityFeed
from firstapp.api.views import (
                                api_community_list_view,
                                api_community_detail_view,
                                api_community_detail_view_class,
                                api_community_update_view,
                                api_community_update_view_class,
                                api_community_delete_class,
                                api_community_create_view_class
                                )

from firstapp.api.views import api_comment_create_view_class, api_post_create_view_class, api_post_list_view, api_comment_list_view

app_name = "firstapp"

urlpatterns = [
     # List View
     path("", api_community_list_view.as_view(), name="all_community_list_view"),
     path("post/", api_post_list_view.as_view(), name="all_post_list_view"),
     path("comment/", api_comment_list_view.as_view(), name="all_comment_list_view"),
     # Create View
     path("create/", api_community_create_view_class.as_view(), name="community_create"),
     path("create/post/", api_post_create_view_class.as_view(), name="post_create"),
     path("create/comment/", api_comment_create_view_class.as_view(), name="comment_create"),
     # Detail Views
     path("<int:community_id>", api_community_detail_view, name="community_detail_function"), # Test
     path("detail/<pk>/", api_community_detail_view_class.as_view(), name="community_detail_class"), # Main Driver
     # Update Views
     path("<int:community_id>/update/", api_community_update_view, name="community_update_function"), # Test
     path("update/<pk>/", api_community_update_view_class.as_view(), name="community_update_class"), # Main Driver

     # Delete View
     path("delete/<pk>/", api_community_delete_class.as_view(), name="community_delete"),

     path('feeds/', CustomJSONActivityFeed.as_view(), name='mystream')
]


