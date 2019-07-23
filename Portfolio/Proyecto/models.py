from django import forms

class ProyectForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=100)
    Description = forms.CharField(label='Description', max_length=1000)
    Website = forms.URLField(max_length=255)
    date = form.DateField(auto_now=False, auto_now_add=False) #nombre de la variable dudoso usar algo mas espeficifico


class GalleryForm(forms.Form):
	#Photo = forms.ImageField(upload_to = 'Gallery' , default= "default.png") #hacer carpeta assets y "Gallery" en assets
	Proyect = forms.OneToOneField(ProyectForm, on_delete=models.CASCADE, default = 0)