from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
 
from firstapp.models import Community, Post_Type
from firstapp.api.serializers import CommunitySerializer, Post_TypeSerializer

# List of all communities, LISTAPIVIEW use
class api_community_list_view(ListAPIView):
    
    serializer_class = CommunitySerializer
    def get_queryset(self):
        communities = Community.objects.order_by("-community_creation_date")
        return communities

# Detail view of any community, function based view.
@api_view(["GET"])
def api_community_detail_view(request,community_id):

    try:
        community = Community.objects.get(pk = community_id)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == "GET":
        serializer = CommunitySerializer(community)
        return Response(serializer.data)