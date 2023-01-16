from django.shortcuts import render
from pytube import *


def index(request):
    if request.method == 'POST':
        link = request.POST['link']
        video = YouTube(link)
        if 'download_low' in request.POST:
            stream = video.streams.get_lowest_resolution()
        elif 'download_high' in request.POST:
            stream = video.streams.get_highest_resolution()
        stream.download()
    return render(request, 'downloader_app/index.html')
