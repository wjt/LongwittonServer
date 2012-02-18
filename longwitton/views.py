from longwitton.models import Game
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers
import urllib
import re


def get_game():
    # FIXME: more than one game?
    return Game.objects.all()[0]

def status(request):
    g = get_game()

    title = g.goal[len("http://en.wikipedia.org/wiki/"):]
    r = urllib.urlopen(
        'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles=' + title)
    json = r.read()
    content = re.search(r'"revisions":\[\{"\*":"(.{1,2000})', json)

    print content.group(1)
    titles = re.findall(r'"title":"[^"]+', json)

    if g.status == 'noone':
        game_status = 'In progress!'
    else:
        game_status = '%s won!' % g.status

    return render_to_response('longwitton/status.html',
        { 'game': g,
          'game_status': game_status,
          'summary': content.group(0),
        })

def reset(request):
    r = urllib.urlopen(
        'http://en.wikipedia.org/w/api.php?format=json&action=query&list=random&rnlimit=3&rnnamespace=0')
    json = r.read()
    print json
    titles = re.findall(r'"title":"[^"]+', json)

    print titles
    urls = map(lambda t: 'http://en.wikipedia.org/wiki/' + t[9:].replace(' ', '_'), titles)
    print urls

    g = get_game()
    g.goal = urls[0]
    g.chasee_start_page = urls[1]
    g.chasee_current_page = urls[1]

    g.chaser_start_page = urls[2]
    g.chaser_current_page = urls[2]

    g.status = 'noone'
    g.save()

    return HttpResponse("hi")

def make_plain_response():
    r = HttpResponse(content_type='text/plain')
    r['Access-Control-Allow-Origin'] = '*'
    return r

def chasee_current(request):
    g = get_game()

    r = make_plain_response()

    if g.status != 'noone':
        r.write(g.status)
    else:
        r.write(g.chasee_current_page)

    return r

def chasee_target(request):
    g = get_game()
    r = make_plain_response()

    if g.status != 'noone':
        r.write(g.status)
    else:
        r.write(g.goal)

    return r

# Modifies state with a GET! Bad me.
def chasee_update(request, new_url):
    g = get_game()
    g.chasee_current_page = new_url

    if g.goal == new_url:
        g.status = 'chasee'

    g.save()
    r = make_plain_response()
    r.write('fine')
    return r

# Modifies state with a GET! Bad me.
def chaser_update(request, new_url):
    g = get_game()
    g.chaser_current_page = new_url

    if new_url == g.chasee_current_page:
        g.status = 'chaser'

    g.save()
    r = make_plain_response()
    r.write('fine')
    return r
