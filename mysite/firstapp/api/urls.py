from django.urls import path
from firstapp.api.views import api_community_detail_view, api_community_list_view

app_name = "firstapp"

urlpatterns = [
     path("", api_community_list_view.as_view(), name="all_community_list_view"),
     path("<int:community_id>", api_community_detail_view, name="community_detail")
]


 