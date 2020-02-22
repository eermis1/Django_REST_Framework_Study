from django.urls import path
from firstapp.api.views import api_community_detail_view

app_name = "firstapp"

urlpatterns = [
     path("<int:community_id>", api_community_detail_view, name="community_detail")
]


 