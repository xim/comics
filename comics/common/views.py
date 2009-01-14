import datetime as dt

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from comics.common.models import Comic
from comics.common.utils.comic_strips import get_comic_strips_struct
from comics.common.utils.navigation import get_navigation

# Generic views

def generic_show(request, queryset, page, latest=False, extra_context=None):
    """Generic view for showing comics"""

    comics = get_comic_strips_struct(
        queryset,
        latest=latest,
        start_date=page.get('start_date', None),
        end_date=page.get('end_date', None))

    kwargs = {
        'page': page,
        'comics': comics,
    }
    if extra_context is not None:
        kwargs.update(extra_context)
    return render_to_response('common/strip-list.html', kwargs,
        context_instance=RequestContext(request))


### Top comics ###

def top_show(request, year=None, month=None, day=None, days=1):
    """Show top comics from one or more dates"""

    year = year and int(year)
    month = month and int(month)
    day = day and int(day)
    days = days and int(days)
    if not (1 <= days <= settings.COMICS_MAX_DAYS_IN_PAGE):
        raise Http404

    queryset = Comic.objects.all().order_by(
        '-number_of_sets', 'name')[:settings.COMICS_MAX_IN_TOP_LIST]
    page = get_navigation(request, 'top',
        year=year, month=month, day=day, days=days)
    return generic_show(request, queryset, page)

def top_latest(request):
    """Show latest strip for each comic"""

    queryset = Comic.objects.all().order_by(
        '-number_of_sets', 'name')[:settings.COMICS_MAX_IN_TOP_LIST]
    page = get_navigation(request, 'top', days=1, latest=True)
    return generic_show(request, queryset, page, latest=True)

def top_year(request, year):
    """Redirect to first day of year if not in the future"""

    if int(year) > dt.date.today().year:
        raise Http404
    else:
        return HttpResponseRedirect(reverse('top-date', kwargs={
            'year': year,
            'month': 1,
            'day': 1,
        }))


### One comic ###

def comic_list(request):
    """List all available comics"""

    kwargs = {'comics': Comic.objects.all()}
    return render_to_response('common/comic-list.html', kwargs,
        context_instance=RequestContext(request))

def comic_show(request, comic, year=None, month=None, day=None, days=1):
    """Show one specific comic from one or more dates"""

    year = year and int(year)
    month = month and int(month)
    day = day and int(day)
    days = days and int(days)
    if not (1 <= days <= settings.COMICS_MAX_DAYS_IN_PAGE):
        raise Http404

    comic = get_object_or_404(Comic, slug=comic)
    queryset = [comic]
    page = get_navigation(request, 'comic', instance=comic,
        year=year, month=month, day=day, days=days)
    return generic_show(request, queryset, page)

def comic_latest(request, comic):
    """Show latest strip from comic"""

    comic = get_object_or_404(Comic, slug=comic)
    queryset = [comic]
    page = get_navigation(request, 'comic', instance=comic, days=1, latest=True)
    return generic_show(request, queryset, page, latest=True)

def comic_year(request, comic, year):
    """Redirect to first day of year if not in the future"""

    if int(year) > dt.date.today().year:
        raise Http404
    else:
        return HttpResponseRedirect(reverse('comic-date', kwargs={
            'comic': comic,
            'year': year,
            'month': 1,
            'day': 1,
        }))


### Other views ###

def about(request):
    return render_to_response('common/about.html',
        context_instance=RequestContext(request))

def robots(request):
    return HttpResponse('User-Agent: *\nDisallow: /\n', mimetype='text/plain')
