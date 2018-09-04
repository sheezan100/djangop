from django.http import HttpResponse
from .models import Album,Songs
#from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404

def index(request):
    all_album=Album.objects.all()
    #template1=loader.get_template('music/index.html')
    context={
        'all_album':all_album,
    }

    return render(request, 'index.html', context)


def details(request, album_id):
    album=get_object_or_404(Album, pk=album_id)
    return render(request, 'details.html', {'album':album})

def favorite(request, album_id):
    album=get_object_or_404(Album, pk=album_id)
    try:
         selected_song=album.songs_set.get(pk=request.post['song'])

    except(KeyError, Songs.DoesNotExist):
        return render(request, 'details.html',{
            'album':album,
            'error_message':"you didn,t select valid song"
        })

    else:
        selected_song.is_fav=True
        selected_song.save()

