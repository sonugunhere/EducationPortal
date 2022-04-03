
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.username







class Contact(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    massage = models.TextField(blank=True)


    def __str__(self):
        return self.name
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title+" "+self.author.username
from django.contrib.auth.models import User