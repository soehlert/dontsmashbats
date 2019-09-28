from django.contrib import admin

from .models import BatFact


# Register your models here.
class BatFactAdmin(admin.ModelAdmin):
	model = BatFact
	list_display = ['title', 'short_description', 'type', 'date_added']
	search_fields = ['type', 'fact']
	list_filter = ['type']


admin.site.register(BatFact, BatFactAdmin)