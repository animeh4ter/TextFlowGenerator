from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from .script import UserVideo
import moviepy.editor as mpy
from moviepy.video.tools.segmenting import findObjects


def user_video(request):
    text = request.GET.get('text')
    if text:
        video = UserVideo(str(text))
        video.video_maker()
        response = FileResponse(open(f'{text}.mp4', 'rb'), content_type='application/video.mp4')
        return response
    else:
        return HttpResponse('<h1>There is no text...</h1>')