from django import forms
from django.db import models

class Proyect(models.Model):
	"""
	model that will give information 
	about the different projects that 
	we have worked on, a link if it 
	is a web page or, alternatively, 
	an executable
	"""
	name = models.CharField(max_length=100)
	cover_page = models.ImageField(upload_to='cover_pages', default="Kalwak.svg")
	description = models.CharField(max_length=1000)
	website = models.URLField(max_length=255)
	date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return f"Name: {self.name}, Link: {self.website}"

class Gallery(models.Model):
	"""
	a photo that will reference a project
	(many photos will reference a single project)
	"""
	photo = models.ImageField(upload_to='Gallery' , default="Kalwak.svg")
	proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE, default=0)
	def __str__(self):
		return f"Name: {self.photo.name}"

