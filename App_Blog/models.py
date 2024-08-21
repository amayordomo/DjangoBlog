from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_posts')
    blog_title = models.CharField(max_length=264, verbose_name="Enter a Title")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="What is on your mind?")
    blog_image = models.ImageField(upload_to="blog_images", verbose_name="Blog Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blogs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker_users')
