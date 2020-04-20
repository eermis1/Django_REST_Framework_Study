from rest_framework import serializers
from firstapp.models import Community, Post, Comment

# Building model serializers for Community

# --------------------------------------------------  Create View Serializers  ------------------------------------------------------
from rest_framework.serializers import ModelSerializer

class CommunitySerializer_ForCreate(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ["community_name", "community_description", "community_tag"]

class PostSerializer_ForCreate(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["post_name", "post_description", "post_tag"]

class CommentSerializer_ForCreate(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["comment_creation_date", "comment_modification_date", "comment_builder"]

# --------------------------------------------------  Detail View Serializers -------------------------------------------------------

class CommunitySerializer_ForDetail(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ["id", "community_builder", "community_name", "community_description", "community_tag",
                  "community_creation_date", "community_modification_date", "community_slug",
                  "community_image", "community_modifiedby"]


# --------------------------------------------------  Update View Serializers  -----------------------------------------------------

class CommunitySerializer_ForUpdate(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ["community_name", "community_tag", "community_image"]


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
        fields = "__all__"


class PostSerializer_ForList(serializers.ModelSerializer):

    # to do __> hyperlinked Identity Field

    post_builder_name = serializers.SerializerMethodField(method_name="username")

    def username(self, obj):
        return str(obj.post_builder.username)

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer_ForList(serializers.ModelSerializer):

    # to do __> hyperlinked Identity Field

    comment_builder_name = serializers.SerializerMethodField(method_name="username")

    def username(self, obj):
        return str(obj.comment_builder.username)

    class Meta:
        model = Comment
        fields = "__all__"

# --------------------------------------------------  Delete View Serializers -------------------------------------------------------

class CommunitySerializer_ForDelete(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ["id", "community_builder", "community_name", "community_description", "community_tag",
                  "community_tag_wiki", "community_creation_date", "community_modification_date", "community_slug",
                  "community_image", "community_modifiedby"]


# --------------------------------------------------  Other Serializers  -------------------------------------------------------

# Building model serializers for Post

class PostSerializer(serializers.Serializer):
    post_name = serializers.CharField(max_length=100)
    post_description = serializers.CharField(max_length=200)
    post_tag = serializers.CharField(max_length=150)

# Building model serializers for Post


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["comment_creation_date", "comment_modification_date"]
