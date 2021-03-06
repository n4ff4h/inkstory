from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from taggit.managers import TaggableManager
from froala_editor.fields import FroalaField


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    # model.CASCADE: will delete all posts related to the user, if user is deleted
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    tags = TaggableManager()
    snippet = models.CharField(max_length=255)
    body = FroalaField()

    likes = models.ManyToManyField(User, related_name="blog_posts")
    post_date = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # Redirect to post detail page for the specified post id
        return reverse('post_detail', args=(self.slug,))
