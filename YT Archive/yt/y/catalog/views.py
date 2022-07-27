from django.shortcuts import render
from .models import Video, Channel
from django.db.models import Q
from django.core.paginator import Paginator 
import timeit

# Create your views here.
def index(request):

    num_video = Video.objects.all().count()
    num_channel = Channel.objects.count()

    context = {
        'num_video': num_video,
        'num_channel': num_channel,
    }
    return render(request, 'index.html', context=context)

from django.views import generic

class VideoListView(generic.ListView):
    model = Video
    paginate_by = 30

class VideoDetailView(generic.DetailView):
    model = Video

from django.shortcuts import get_object_or_404

def video_detail_view(request, primary_key):
    video = get_object_or_404(Video, pk=primary_key)
    return render(request, 'catalog/video_detail.html', context={'video': video})

class ChannelListView(generic.ListView):
    model = Channel
    paginate_by = 30

class ChannelDetailView(generic.DetailView):
    model = Channel

def channel_detail_view(request, primary_key):
    channel = get_object_or_404(Channel, pk=primary_key)
    return render(request, 'catalog/channel_detail.html', context={'channel': channel})

def get_video(request):

    if 'q_v' in request.GET and request.GET['q_v']:
        query = request.GET.get('q_v')
        request.session['query_v'] = query
    else:
        if request.GET.get('submit') == 'Search':
            query = ''
            request.session['query_v'] = query
        else:
            query = request.session.get('query_v')

    t0 = timeit.default_timer()
    video_list = Video.objects.filter(Q(video_title__icontains = query) | Q(video_description__icontains = query))
    t1 = timeit.default_timer() - t0
        
    paginator = Paginator(video_list, 30)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context={
        "video_list":page_obj,
        "video_list_len":video_list.count(),
        "time_elapsed":t1,
        "key":query
    }
    return render(request, 'video_search_results.html', context=context)

def get_channel(request):

    if 'q_c' in request.GET and request.GET['q_c']:
        query = request.GET.get('q_c')
        request.session['query_c'] = query
    else:
        if request.GET.get('submit') == 'Search':
            query = ''
            request.session['query_c'] = query
        else:
            query = request.session.get('query_c')
        

    t0 = timeit.default_timer()
    channel_list = Channel.objects.filter(Q(channel_title__icontains = query) | Q(channel_description__icontains = query))
    t1 = timeit.default_timer() - t0

    paginator = Paginator(channel_list, 30)

    page_number = request.GET.get('page') 

    page_obj = paginator.get_page(page_number)

    context={
        "channel_list":page_obj,
        "channel_list_len":channel_list.count(),
        "time_elapsed":t1,
        "key":query
    }
    return render(request, 'channel_search_results.html', context=context)


    
    

