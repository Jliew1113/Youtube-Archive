from django.db import models
from django.urls import reverse

# Create your models here.
class Video(models.Model):
    id = models.AutoField(primary_key=True, unique=True)

    video_title = models.CharField(max_length = 1000, verbose_name = 'Title')
    channel = models.ForeignKey('Channel', on_delete=models.SET_NULL, null=True)
    video_url = models.URLField(verbose_name = 'Link', max_length = 500)
    video_thumbnail = models.ImageField(upload_to='images/')
    video_description = models.TextField(max_length = 1000000, verbose_name ='Description')
    video_views = models.CharField(max_length = 100, verbose_name = 'Views')
    video_date = models.CharField(max_length = 20, verbose_name = 'Date Published')
    video_likes = models.IntegerField(verbose_name = 'Likes')
    video_dislikes = models.IntegerField(verbose_name = 'Dislikes')
    video_comments = models.TextField(max_length = 1000000, verbose_name = 'Comments')

    def __str__(self):
        """String for representing the Model object."""
        return self.video_title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('video-detail', args=[str(self.id)])

class Channel(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length = 100)

    channel_title = models.CharField(max_length = 100, verbose_name = 'Title')
    channel_url = models.URLField(verbose_name = 'Link', max_length = 500)
    channel_thumbnail = models.ImageField(upload_to='images/')
    channel_description = models.TextField(max_length = 1000000, verbose_name ='Description')
    channel_subscribers = models.CharField(max_length = 100, verbose_name = 'Subscribers')

    def __str__(self):
        """String for representing the Model object."""
        return self.channel_title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('channel-detail', args=[str(self.id)])