from rest_framework import serializers
from firstapp.models import Community, Post


# Building model serializers for Community

# --------------------------------------------------  Create View Serializers  ------------------------------------------------------

class CommunitySerializer_ForCreate(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ["community_name", "community_description", "community_tag", "community_tag_wiki"]


# --------------------------------------------------  Detail View Serializers -------------------------------------------------------

class CommunitySerializer_ForDetail(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ["id", "community_builder", "community_name", "community_description", "community_tag",
                  "community_tag_wiki", "community_creation_date", "community_modification_date", "community_slug",
                  "community_image", "community_modifiedby"]


# --------------------------------------------------  Update View Serializers  -----------------------------------------------------

class CommunitySerializer_ForUpdate(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ["community_name", "community_tag", "community_tag_wiki", "community_image"]


# --------------------------------------------------  List/Index View Serializers -------------------------------------------------------

class CommunitySerializer_ForList(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='firstapp:community_detail_class',
        lookup_field='pk')  # Video-20 HyperLinked Identity Field

    community_builder_name = serializers.SerializerMethodField(method_name="username")

    def username(self, obj):
        return str(obj.community_builder.username)

    class Meta:
        model = Community
        fields = ["id", "community_builder", "community_builder_name", "community_name", "community_description",
                  "community_tag", "community_tag_wiki", "community_slug", "url", "community_creation_date",
                  "community_modification_date", "community_image", "community_modifiedby"]


# --------------------------------------------------  Delete View Serializers -------------------------------------------------------

class CommunitySerializer_ForDelete(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ["id", "community_builder", "community_name", "community_description", "community_tag",
                  "community_tag_wiki", "community_creation_date", "community_modification_date", "community_slug",
                  "community_image", "community_modifiedby"]


# Building model serializers for Post

class PostSerializer(serializers.Serializer):
    post_name = serializers.CharField(max_length=100)
    post_description = serializers.CharField(max_length=200)
    post_tag = serializers.CharField(max_length=150)
