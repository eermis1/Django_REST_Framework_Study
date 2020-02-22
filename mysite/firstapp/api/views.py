from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
 
from firstapp.models import Community, Post_Type
from firstapp.api.serializers import CommunitySerializer, Post_TypeSerializer

@api_view(["GET"])
def api_community_detail_view(request,community_id):

    try:
        community = Community.objects.get(pk = community_id)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == "GET":
        serializer = CommunitySerializer(community)
        return Response(serializer.data)

 