from django.db import models
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
    community_tag_wiki = models.CharField(max_length=400)
    community_creation_date = models.DateTimeField(editable=False, blank=True)
    community_modification_date = models.DateTimeField(editable=False, blank=True)
    community_slug = models.SlugField(max_length=150, unique=True, editable=False) 
    community_modifiedby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="modified_by")
    # Defining Max Length is critical as it raises "DatabaseError: value too long for type character varying(100)" if max_length not specified 
    community_image = models.ImageField(upload_to = "community") # To do so, pip install Pillow

    def get_slug(self):
        # Unique slug creation
        # Replace turkish characters with english ones. 
        slug = slugify(self.community_name.replace("ı","i"))
        unique = slug 
        number = 1

        while Community.objects.filter(community_slug=unique).exists():
            unique  = "{}-{}".format(slug,number) # If slug "evren" exists then make new slug as "evren-1"
            number =+ 1

        return unique

    def save(self, *args, **kwargs):
        # If Self.id does not exist then it is a creation --> creation date = timezone.now()
        if not self.id:
            self.community_creation_date = timezone.now()
        
        # If Self.id exists then it is a modification --> modification date = timezone.now()
        self.community_modification_date = timezone.now()
        self.community_slug = self.get_slug()
        # action.send(str(self.community_builder), verb="Community Has Been Created", target=self.id)
        return super(Community, self).save(*args,**kwargs)

    def __str__ (self):
        return self.community_name + "  " + str(self.community_builder)

    # def __str__ (self):
    #     return ("Community ID : " + str(self.id) +  "     " + "Community Name : " + self.community_name)
    
class Post_Type(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name = "community")
    post_type_title = models.CharField(max_length=100)
    post_type_description = models.CharField(max_length=200)
    post_type_tag = models.CharField(max_length=150)
    post_type_owner =models.ForeignKey(User, on_delete=models.PROTECT)
    post_type_creation_date = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    post_type_slug = models.SlugField(blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('community:posttype_postobject_detail', kwargs={"pk" : self.pk})

    def __str__ (self):
        return (self.post_type_title)

    # def __str__ (self):
    #     return ("\nPost id : " + str(self.id) + "\nPost Title : " + self.post_type_title +  "\nPost Description : " + self.post_type_description +  "\nPost Tag : "  
    #             + self.post_type_tag + "\nForm Field:" + "\nPost Community id : " + str(self.community))
