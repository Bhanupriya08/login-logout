from django.db import models

# Create your models here.

class Country(models.Model):
	country = models.CharField(max_length=200)



	def __str__(self):
		return self.country

    


class State(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	state = models.CharField(max_length=200)

	def __str__(self):
		return self.state

class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=100)
    file = models.FileField(upload_to='country/book/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title