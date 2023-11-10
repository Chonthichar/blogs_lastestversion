from django.db import models
from django.utils.timezone import make_aware
from django.utils import timezone
from datetime import datetime
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
from django.db import models
from django.utils import timezone

# Add a Rich text editor to a Django blog
# from ckeditor.fields import RichTextField




class Fields(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    authorHidden = models.CharField(max_length=255, null=True)
    updated_on = models.DateTimeField(default=timezone.now)
    # content = RichTextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    # content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images_uploaded', null=True)
    video = models.FileField(upload_to='videos_uploaded', null=True)
    like = models.ManyToManyField(User, related_name='blog_like') # assiciate many together

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category_blog = models.CharField(max_length=255, default='coding')

    def __str__(self):
        return self.title + ' | ' + str(self.user)  # an objects turn in to string

    def total_likes(self):
        return self.like.count()

class Category_blog(models.Model):
    name = models.CharField(max_length=255)

# associate with user app with this
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) #when we delete user automatically delete
    bio = models.TextField()
    picture_profile =models.ImageField(null=True, blank=True, upload_to='images/profile/')

    facebook_url = models.CharField(max_length=255, null=True, blank=True,)
    twitter_url = models.CharField(max_length=255, null=True, blank=True, )
    instagram_url = models.CharField(max_length=255, null=True, blank=True, )


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('blog:home')

class Add_comment(models.Model):
    # we call comment then grab all the comment
    post_title = models.ForeignKey(Fields, related_name="comments", on_delete=models.CASCADE) #automatically delete blog post that
    body = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.post_title.title, self.name)
#     will show post title that we are comment on


# a. title (character field)
# b. author (character field)
# c. updated_on (date/time field)
# d. content (text field)
# e. created_on (date/time field)
# f. image (img field)
# g. video (video field)

