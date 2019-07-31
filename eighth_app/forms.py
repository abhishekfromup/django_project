# forms.py
from django import forms
from django.core import validators
from .models import *

def manual_name_validation(value):
	if value.isalpha() != True:
		raise forms.ValidationError('only alphabets are allowed in name..')



class FeedbackForm(forms.Form):
    name = forms.CharField(validators = [validators.MinLengthValidator(3), manual_name_validation])
    course = forms.CharField()
    email = forms.EmailField()
    feedback = forms.CharField(widget = forms.Textarea)

    def clean_email(self):
	    if self.cleaned_data['email'].split('@')[1] != 'gmail.com':
		    raise forms.ValidationError("Email doesn't belong to gmail domain...")
	    return self.cleaned_data['email']
	    

class ModelFormCreation(forms.ModelForm):
	class Meta:
		model = StudentFeedback
		fields = '__all__'