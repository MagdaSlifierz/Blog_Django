
from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

#create ManagerPublisher who can see all posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

#Post model allows to store post in database


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self): #method to return strin to easy read info from object
        return self.name
    
    #not sure
    def get_absolute_url(self):
        #return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
        return reverse('home')
    

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) #one to one assisiate with user from django
    bio = models.TextField()
    profie_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
    facebook_url = models.CharField(max_length=250, null=True, blank=True)
    linkedIn_url = models.CharField(max_length=250, null=True, blank=True)
    instagram_url = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self): #method to return strin to easy read info from object
        return str(self.user)
    
    
class Post(models.Model):
 
    class Status(models.TextChoices): #that is a subclass of the class 
        #available choices are:
        DRAFT = "DF", "Draft" #make a draft
        PUBLISHED = "PB", "Published" #status for poblish post

    title = models.CharField(max_length=250) # this stres title of blog
    header_image = models.ImageField(null=True, blank=True, upload_to='images/') #allow to not have image if I don't want it
    slug = models.SlugField(max_length=250, unique_for_date='publish') #slug field short label djn-reih-jazz

    #ADD MANY TO ONE RELATIONSHIP Author to Post each post written by user
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #ondelete tells if author is deleted her posts are deleted
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField() #this stores body of blog
    publish = models.DateTimeField(default=timezone.now) #published at specific time
    created = models.DateTimeField(auto_now_add=True) #when the post was creates
    updated = models.DateTimeField(auto_now=True) #when data was updates
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    likes = models.ManyToManyField(User, related_name='blog_posts' )

    objects = models.Manager()
    published = PublishedManager() #adding manager who can see posts
    class Meta: #this is a metadata ordering attribiute
        ordering = ['-publish'] #blog from newest to oldest
        indexes = [
            models.Index(fields=['-publish']),
        ]


    def __str__(self): #method to return strin to easy read info from object
        return self.title

    def total_likes_func(self):
        return self.likes.count()
    
    #not sure
    def get_absolute_url(self):
        #return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
        return reverse('home')
    
    
    
    
    
    