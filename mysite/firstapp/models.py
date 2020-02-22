from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import Permission, User
from django.conf import settings
import datetime
from django.utils import timezone


class Community(models.Model):
    community_builder = models.ForeignKey(User, on_delete=models.PROTECT)
    community_name = models.CharField(max_length=100)
    community_description = models.CharField(max_length=200)
    community_tag = models.CharField(max_length=150)
    community_tag_wiki = models.CharField(max_length=400)
    community_creation_date = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    community_slug = models.SlugField(blank=True, unique=True)
    
    def __str__ (self):
        return ("Community ID : " + str(self.id) +  "     " + "Community Name : " + self.community_name)

    def get_absolute_url(self):
         return reverse('community:community_posttype_detail', kwargs={"pk" : self.pk})

    def was_published_recently(self):
        #Last 2 Days Of Communities --> Recent
        return self.community_creation_date >= timezone.now()-datetime.delta(days=2)
    
class Post_Type(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    post_type_title = models.CharField(max_length=100)
    post_type_description = models.CharField(max_length=200)
    post_type_tag = models.CharField(max_length=150)
    post_type_owner =models.ForeignKey(User, on_delete=models.PROTECT)
    post_type_creation_date = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    post_type_slug = models.SlugField(blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('community:posttype_postobject_detail', kwargs={"pk" : self.pk})


    def __str__ (self):
        return ("\nPost id : " + str(self.id) + "\nPost Title : " + self.post_type_title +  "\nPost Description : " + self.post_type_description +  "\nPost Tag : "  
                + self.post_type_tag + "\nForm Field:" + "\nPost Community id : " + str(self.community))
