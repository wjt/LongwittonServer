from longwitton.models import Game
from django.shortcuts import render_to_response
from django.http import HttpResponse

def get_game():
    # FIXME: more than one game?
    return Game.objects.all()[0]

def status(request):
    g = get_game()

    if g.status == 'noone':
        game_status = 'In progress!'
    else:
        game_status = '%s won!' % g.status

    return render_to_response('longwitton/status.html',
        { 'game': g,
          'game_status': game_status,
        })

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
    return HttpResponse('Fine.')

# Modifies state with a GET! Bad me.
def chaser_update(request, new_url):
    g = get_game()
    g.chaser_current_page = new_url

    if new_url == g.chasee_current_page:
        g.status = 'chaser'

    g.save()
    return HttpResponse('Fine.')
