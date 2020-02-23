from rest_framework import serializers
from firstapp.models import Community, Post_Type



# Building model serializers for Community and Post Type
class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community 
        fields = ["id", "community_builder", "community_name", "community_description", "community_tag", "community_creation_date"]


class Post_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Type
        fields = ["id", "community", "post_type_title", "post_type_description", "post_type_tag", "post_type_creation_date"]