from django import forms
from .models import Product


class ContactForm(forms.Form):

	yourname = forms.CharField(max_length=100, label='Your name')
	email = forms.EmailField(required=False, label='Your email')
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea) #textfield