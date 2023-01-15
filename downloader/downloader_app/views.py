from django.shortcuts import render
from pytube import *


def index(request):
    if request.method == 'POST':
        link = request.POST['link']
        video = YouTube(link)
        stream = video.streams.get_lowest_resolution()
        stream.download()

    return render(request, 'downloader_app/index.html')
