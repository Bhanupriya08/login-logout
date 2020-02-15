from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person,Country,State,Book
from .forms import PersonForm , BookForm
from django.core import serializers
from django.http import HttpResponse
import json as simplejson
from django.core.files.storage import FileSystemStorage

# Create your views here.


def data(request):
	country_list = Country.objects.all()
	return render(request,'country/person_list.html',{'country_list':country_list})

def all_json_models(request, brand):
	current_country = Country.objects.get(country_id=country)
	models = State.objects.all().filter(country_id=current_country)
	json_models = serializers.serialize("json", models)
	return HttpResponse(json_models)

def getdetails(request):
    #country_name = request.POST['country_name']
    if request.is_ajax():
    	country_name =  request.GET['country']  
    	#print(country_name)
    	result_set = []
    	all_cities = []
    	country = str(country_name)
    	#print(answer)
    	selected_country = Country.objects.get(country=country)
    	print(selected_country)
    	all_states = selected_country.state_set.all()
    	for state in all_states:
        	print (state.state)
        	result_set.append({'name': state.state})
    	return HttpResponse(simplejson.dumps(result_set),content_type='application/json')

#******to upload file *****

def upload(request):
	if request.method == 'POST':
		form = BookForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("country:book_list")

	form = BookForm()
	return render(request,'country/upload_form.html',{'form':form})


def booklist(request):
	books = Book.objects.all()
	return render(request,'country/book_list.html',{'books':books})



def person(request):
	form = PersonForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			name = form.cleaned_data['name']
			birthdate = form.cleaned_data['birthdate']
			country = form.cleaned_data['country']
			state = form.cleaned_data['state']
			data = {
			'name' : name, 
			}
			Person.objects.create(Name=name,birthdate=birthdate,country=country,state=state)
			Person.save()


	
	return render(request,'country/person_list.html',{'form':form})

def load_states(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'country/city_dropdown_list_options.html', {'states': states})
"""class PersonListView(ListView):
    model = Person
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    
    success_url = reverse_lazy('person_list')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    #fields = ('name', 'birthdate', 'country', 'state')
    success_url = reverse_lazy('person_list')"""