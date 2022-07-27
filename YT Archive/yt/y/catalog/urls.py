from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', views.VideoListView.as_view(), name='videos'),
    path('video/<int:pk>', views.VideoDetailView.as_view(), name='video-detail'),
    path('channels/', views.ChannelListView.as_view(), name='channels'),
    path('channel/<path:pk>', views.ChannelDetailView.as_view(), name='channel-detail'),
    path('video-search/', views.get_video, name='video_search_results'),
    path('channel-search/', views.get_channel, name='channel_search_results'),
]