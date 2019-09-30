from django.db import models
from django.template.defaultfilters import truncatechars
from django.db.models.signals import pre_delete

import cloudinary


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

	fact = models.TextField(max_length=300, unique=True)
	title = models.CharField(max_length=75, null=True)
	date_added = models.DateField(auto_now_add=True)
	credit = models.URLField()
	img = cloudinary.CloudinaryImage('img')
	type = models.CharField(max_length=2, choices=fact_types, default=OTHER)

	def __str__(self):
		return f"{self.title}"

	@property
	def short_description(self):
		return truncatechars(self.fact, 50)

	@receiver(pre_delete, sender=BatFact)
	def photo_delete(sender, instance, **kwargs):
		cloudinary.uploader.destroy(instance.img.public_id)
