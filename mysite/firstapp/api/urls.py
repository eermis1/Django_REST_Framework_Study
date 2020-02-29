from django.urls import path
from firstapp.api.views import (api_community_detail_view, 
                                api_community_detail_view_class,
                                api_community_list_view, 
                                api_community_update_view, 
                                api_community_delete_view,
                                class_api_community_update_view)

app_name = "firstapp"

urlpatterns = [
     path("", api_community_list_view.as_view(), name="all_community_list_view"),
     path("<int:community_id>", api_community_detail_view, name="community_detail_function"),
     path("detail/<pk>/", api_community_detail_view_class.as_view(), name="community_detail_class"),
     path("update/<int:community_id>/", api_community_update_view, name="community_update"),
     path("<int:community_id>/update/", api_community_update_view, name="community_update_class"),
     path("delete/<int:community_id>/", api_community_delete_view, name="community_delete")
]


 