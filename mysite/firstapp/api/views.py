from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from firstapp.models import Community
from firstapp.api.paginations import Community_Pagination
from firstapp.api.permissions import IsOwner
from rest_framework.permissions import (
                                        IsAuthenticated,
                                        IsAdminUser
                                        )

from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateAPIView,
                                     CreateAPIView)

from firstapp.api.serializers import (CommunitySerializer_ForCreate,
                                      CommunitySerializer_ForDetail,
                                      CommunitySerializer_ForUpdate,
                                      CommunitySerializer_ForList,
                                      CommunitySerializer_ForDelete)

# -------------------------------------------------- List/Index View --------------------------------------------------------------------

class api_community_list_view(ListAPIView):

    serializer_class = CommunitySerializer_ForList
    pagination_class = Community_Pagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["community_name"] # How to filter id?
    # https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains buradan bulunabilir

    def get_queryset(self):
        communities = Community.objects.order_by("-community_creation_date")
        return communities

# -------------------------------------------------- Detail View --------------------------------------------------------------------

# Function based view.
@api_view(["GET", ]) # GET is used for list operations
def api_community_detail_view(request,community_id):

    try:
        community = Community.objects.get(pk = community_id)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CommunitySerializer_ForDetail(community)
        return Response(serializer.data)

# Class based view.
class api_community_detail_view_class(RetrieveAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer_ForDetail
    lookup_field = 'pk' # Pk has to be added to URLs as well.


# -------------------------------------------------- Update View --------------------------------------------------------------------

# Function based view.
@api_view(["PUT", ]) # PUT is used for update operations
def api_community_update_view(request,community_id):

    try:
        community = Community.objects.get(pk = community_id)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = CommunitySerializer_ForUpdate(community, data=request.data)
        data = {} # Refers to Context in usual views.
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update Successful" # We send only Update Successful after update therefore we addedd this.
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class based view.
class api_community_update_view_class(RetrieveUpdateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer_ForUpdate
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    # Modified By Feature
    def perform_update(self, serializer):
        serializer.save(community_modifiedby=self.request.user)


# -------------------------------------------------- Delete View --------------------------------------------------------------------

# Function based view.
@api_view(["Delete", ]) # DELETE is used for delete operations
def api_community_delete_view(request,community_id):

    try:
        community = Community.objects.get(pk = community_id)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = Community.delete()
        data = {} # Refers to Context in usual views.
        if operation:
            data["success"] = "Update Successful" # We send only Update Successful after update therefore we addedd this.
        else:
            data["failure"] = "Update Failed"
            return Response(data=data)
        return Response(data=data)

class api_community_delete_class(DestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer_ForDelete
    lookup_field = 'pk'
    permission_classes = [IsOwner]

# -------------------------------------------------- Create View --------------------------------------------------------------------

class api_community_create_view_class(CreateAPIView):
    serializer_class = CommunitySerializer_ForCreate
    permission_classes = [IsAuthenticated]

    # Saves the Community Builder
    # Mixin Functions --> https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview
    def perform_create(self, serializer):
        serializer.save(community_builder=self.request.user)
        # Postman still requests commmunity_builder but on the standart web link, community_builder name already exists by default.

