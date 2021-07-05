from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Information


class users(UserCreationForm):
	# emriLenda = forms.CharField()
	email = forms.EmailField()
	class Meta:
		model = User
		labels = {
			"username": "Username",
			"email": "Email",
			"first_name":"Emri",
			"last_name":"Mbiemri",
			"password1":"Password",
			"password2":"Konfirmoni passwordin",
        }
		fields = ['username','email','first_name','last_name','password1','password2']


class addInfo(forms.ModelForm):

	class Meta:
		model = Information
		labels = {
			"IdContinents": "Kontinenti",
			"IdState": "Shteti",
			"IdCategorie":"Kategoria",
			"Title":"Titulli",
			"Information":"Informacioni",
			"Photo":"Foto",
        }
		fields = ['IdContinents','IdState','IdCategorie','Title','Information','Photo']

class ApproveInfo(forms.ModelForm):

	confirm = forms.BooleanField()

	class Meta:
		model = Information
		labels = {
			"confim": "Confirm",
        }
		fields = ['confirm']
