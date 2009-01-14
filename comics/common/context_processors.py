from django.conf import settings

from comics.common.models import Comic

def all_comics(request):
    """Add an all_comics queryset to the template context"""

    return {'all_comics': Comic.objects.all()}
