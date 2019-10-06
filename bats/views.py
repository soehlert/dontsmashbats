from django.http import HttpResponse
from django.views.generic import ListView

from dontsmashbats import settings
from .models import BatFact


# Create your views here.
class HomeView(ListView):
    """View for our home page"""
    template_name = 'base.html'
    model = BatFact

    def get_queryset(self):
        return BatFact.objects.all()


def acme_challenge(request):
    return HttpResponse(settings.ACME_CHALLENGE_CONTENT)
