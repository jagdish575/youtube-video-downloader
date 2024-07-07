from django.shortcuts import render, redirect
from django.http import HttpResponse
from pytube import YouTube
from .models import Video
import os
import tempfile



def home(request):
    return render(request, 'home.html')


def download(request):
    if request.method == 'POST':
        video_url = request.POST['video_url']
        save_path = request.POST.get('save_path', None) 
        try:
            yt = YouTube(video_url)
            video = yt.streams.get_highest_resolution()
            if save_path:
                save_dir = os.path.dirname(save_path)
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
            else:
                save_dir = os.path.join('media/videos')
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                safe_filename = 'videos'
                save_path = os.path.join(save_dir, safe_filename + '.mp4')
            video.download(output_path=save_path)
            return redirect('home')
        except Exception as e:
            return HttpResponse('Error: ' + str(e))
    return redirect('home')