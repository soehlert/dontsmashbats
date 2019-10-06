from django.db import models
from django.template.defaultfilters import truncatechars
from PIL import Image as Img


# Create your models here.
class BatFact(models.Model):
	"""A fact about bats and why you shouldn't smash them"""
	FLIGHT = 'FL'
	SLEEP = 'SL'
	SPECIES = 'SP'
	COMMUNITY = 'CO'
	OTHER = 'OT'
	fact_types = [
		(FLIGHT, 'Flight'),
		(SLEEP, 'Sleep'),
		(SPECIES, 'Species'),
		(COMMUNITY, 'Community'),
		(OTHER, 'Other')
	]

	fact = models.TextField(max_length=750, unique=True)
	title = models.CharField(max_length=75, null=True)
	date_added = models.DateField(auto_now_add=True)
	credit = models.URLField()
	img = models.ImageField()
	type = models.CharField(max_length=2, choices=fact_types, default=OTHER)

	def __str__(self):
		return f"{self.title}"

	@property
	def short_description(self):
		return truncatechars(self.fact, 50)

	def save(self):
		if not self.img:
			return

		super(BatFact, self).save()
		image = Img.open(self.img)
		(width, height) = image.size
		size = (300, 300)
		image = image.resize(size, Img.ANTIALIAS)
		image.save(self.img.path)
