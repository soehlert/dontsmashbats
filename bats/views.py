from django.views.generic import ListView
from .models import BatFact


# Create your views here.
class HomeView(ListView):
	"""View for our home page"""
	template_name = 'base.html'
	model = BatFact

	def get_queryset(self):
		return BatFact.objects.all()