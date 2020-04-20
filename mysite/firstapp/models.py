from django.db import models
from django.db.models.signals import post_save, post_delete
from django.urls import reverse
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import Permission, User
from django.conf import settings
import datetime
from django.utils import timezone
from django.utils.text import slugify
from actstream import registry
from actstream import action


class Community(models.Model):
    community_builder = models.ForeignKey(User, on_delete=models.PROTECT)
    community_name = models.CharField(max_length=100)
    community_description = models.CharField(max_length=200)
    community_tag = models.CharField(max_length=150)
    community_creation_date = models.DateTimeField(editable=False, blank=True)
    community_modification_date = models.DateTimeField(editable=False, blank=True)
    community_slug = models.SlugField(max_length=150, unique=True, editable=False)
    community_modifiedby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="modified_by")
    # Defining Max Length is critical as it raises "DatabaseError: value too long for type character varying(100)" if max_length not specified 
    community_image = models.ImageField(upload_to="community")  # To do so, pip install Pillow

    def get_slug(self):
        # Unique slug creation
        # Replace turkish characters with english ones.
        slug = slugify(self.community_name.replace("ı", "i"))
        unique = slug
        number = 1

        while Community.objects.filter(community_slug=unique).exists():
            unique = "{}-{}".format(slug, number)  # If slug "evren" exists then make new slug as "evren-1"
            number = + 1

        return unique

    def save(self, *args, **kwargs):
        # If Self.id does not exist then it is a creation --> creation date = timezone.now()
        if not self.id:
            self.community_creation_date = timezone.now()

        # If Self.id exists then it is a modification --> modification date = timezone.now()
        self.community_modification_date = timezone.now()
        self.community_slug = self.get_slug()
        return super(Community, self).save(*args, **kwargs)

    def __str__(self):
        return self.community_name


def save_community(sender, instance, **kwargs):
    action.send(instance.community_builder, verb="Has Created A New Community - ", target=instance)


post_save.connect(save_community, sender=Community)


class Post(models.Model):
    post_builder = models.ForeignKey(User, on_delete=models.PROTECT)
    post_name = models.CharField(max_length=100)
    post_description = models.CharField(max_length=200)
    post_tag = models.CharField(max_length=150)
    post_creation_date = models.DateTimeField(editable=False, blank=True)
    post_modification_date = models.DateTimeField(editable=False, blank=True)
    post_slug = models.SlugField(max_length=150, unique=True, editable=False)
    post_modifiedby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="post_modified_by")
    # Defining Max Length is critical as it raises "DatabaseError: value too long for type character varying(100)" if max_length not specified
    post_image = models.ImageField(upload_to="post")  # To do so, pip install Pillow

    def get_slug(self):
        # Unique slug creation
        # Replace turkish characters with english ones.
        slug = slugify(self.post_name.replace("ı", "i"))
        unique = slug
        number = 1

        while Post.objects.filter(post_slug=unique).exists():
            unique = "{}-{}".format(slug, number)  # If slug "evren" exists then make new slug as "evren-1"
            number = + 1

        return unique

    def save(self, *args, **kwargs):
        # If Self.id does not exist then it is a creation --> creation date = timezone.now()
        if not self.id:
            self.post_creation_date = timezone.now()

        # If Self.id exists then it is a modification --> modification date = timezone.now()
        self.post_modification_date = timezone.now()
        self.post_slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.post_name


def save_post(sender, instance, **kwargs):
    action.send(instance.post_builder, verb="Has Created A New Post - ", target=instance)


post_save.connect(save_post, sender=Post)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    comment_builder = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.TextField()
    comment_parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    comment_creation_date = models.DateTimeField(editable=False, blank=True)
    comment_modification_date = models.DateTimeField(editable=False, blank=True)

    class Meta:
        ordering = ("comment_creation_date",)

    def __str__(self):
        return self.post.post_name + " " + self.user.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.comment_creation_date = timezone.now()

        self.comment_modification_date = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def any_children(self):
        return Comment.objects.filter(parent=self).exists()