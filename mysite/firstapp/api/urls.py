from django.urls import path
from firstapp.api.views import (
                                api_community_list_view, 
                                api_community_detail_view, 
                                api_community_detail_view_class,
                                api_community_update_view, 
                                api_community_update_view_class,
                                api_community_delete_view,
                                api_community_create_view_class
                                )

app_name = "firstapp"

urlpatterns = [
     path("", api_community_list_view.as_view(), name="all_community_list_view"),
     # Detail Views
     path("<int:community_id>", api_community_detail_view, name="community_detail_function"), # Test
     path("detail/<pk>/", api_community_detail_view_class.as_view(), name="community_detail_class"), # Main Driver
     # Update Views
     path("<int:community_id>/update/", api_community_update_view, name="community_update_function"), # Test
     path("update/<pk>/", api_community_update_view_class.as_view(), name="community_update_class"), # Main Driver
     # Create View
     path("create/", api_community_create_view_class.as_view(), name="community_create"),   
     # Delete View  
     path("delete/<int:community_id>/", api_community_delete_view, name="community_delete")
]


 