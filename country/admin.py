from django.contrib import admin
from .models import Country,State,Person,Book

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


