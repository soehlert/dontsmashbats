from django.contrib import admin

from .models import BatFact, Charity


# Register your models here.
class BatFactAdmin(admin.ModelAdmin):
	model = BatFact
	list_display = ['title', 'short_description', 'type', 'date_added']
	search_fields = ['type', 'fact']
	list_filter = ['type']


admin.site.register(BatFact, BatFactAdmin)


class CharityAdmin(admin.ModelAdmin):
	model = Charity
	list_display = ['name', 'url']
	search_fields = ['name']


admin.site.register(Charity, CharityAdmin)