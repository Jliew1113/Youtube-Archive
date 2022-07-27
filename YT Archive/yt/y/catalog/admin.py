from django.contrib import admin

# Register your models here.
from .models import Channel, Video

#admin.site.register(Channel)
#admin.site.register(Video)

# Define the admin class
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_thumbnail', 'channel_title', 'channel_url', 'channel_description', 'channel_subscribers')
    fields = ['channel_thumbnail', 'channel_title', 'channel_url', 'channel_description', 'channel_subscribers']

# Register the admin class with the associated model
admin.site.register(Channel, ChannelAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_thumbnail', 'video_title', 'video_url', 'channel', 'video_description', 'video_views', 'video_date', 'video_likes', 'video_dislikes', 'video_comments')
    fields = ['video_thumbnail', 'video_title', 'video_url', 'channel', 'video_description', ('video_views', 'video_date'), ('video_likes', 'video_dislikes'), 'video_comments']

admin.site.register(Video, VideoAdmin)

