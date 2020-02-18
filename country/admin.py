from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.admin import AdminSite
from .models import Country,State,Person,Book


admin.site.unregister(Group)

admin.site.index_title = "Welcome to Jakhar Infotech Portal"
admin.site.site_header = "Jakhar Infotech"   #to change login page header
admin.site.site_title = "Jakhar Infotech Portal"

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = [ 'country']



admin.site.register(Country,CountryAdmin)

class StateAdmin(admin.ModelAdmin):
	model = State
	list_display = [ 'country','state']

	
admin.site.register(State,StateAdmin)
admin.site.register(Person)
admin.site.register(Book)


