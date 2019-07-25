from django import forms

class ProyectForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=100)
    Cover_page = forms.ImageField(upload_to = 'cover_pages' , default= "Kalwak.svg")
    Description = forms.CharField(label='Description', max_length=1000)
    Website = forms.URLField(max_length=255)
    Date = forms.DateField(auto_now=False, auto_now_add=False)

class GalleryForm(forms.Form):
	Photo = forms.ImageField(upload_to = 'Gallery' , default= "Kalwak.svg")
