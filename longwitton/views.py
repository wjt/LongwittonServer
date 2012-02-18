# Create your views here.
from longwitton.models import Page
from django.http import HttpResponse

def make_response():
    r = HttpResponse(content_type='text/plain')
    r['Access-Control-Allow-Origin'] = '*'
    return r

def current(request):
    r = make_response()
    try:
        last_page = Page.objects.all().order_by('-timestamp')[0]
        r.write(last_page.url)
    except Exception, e:
        r.write(e)

    return r

# Modifies state with a GET! Bad me.
def update(request, new_url):
    p = Page(url=new_url)
    p.save()
    return HttpResponse('Fine.')
