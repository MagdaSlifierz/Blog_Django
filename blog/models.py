
from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone


# Create your models here.

#create ManagerPublisher who can see all posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

#Post model allows to store post in database

class Post(models.Model):

    class Status(models.TextChoices): #that is a subclass of the class 
        #available choices are:
        DRAFT = "DF", "Draft" #make a draft
        PUBLISHED = "PB", "Published" #status for poblish post

    title = models.CharField(max_length=250) # this stres title of blog
    slug = models.SlugField(max_length=250) #slug field short label djn-reih-jazz

    #ADD MANY TO ONE RELATIONSHIP Author to Post each post written by user
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    #ondelete tells if author is deleted her posts are deleted


    body = models.TextField() #this stores body of blog
    publish = models.DateTimeField(default=timezone.now) #published at specific time
    created = models.DateTimeField(auto_now_add=True) #when the post was creates
    updated = models.DateTimeField(auto_now=True) #when data was updates
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager() #adding manager who can see posts
    class Meta: #this is a metadata ordering attribiute
        ordering = ['-publish'] #blog from newest to oldest
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self): #method to return strin to easy read info from object
        return self.title