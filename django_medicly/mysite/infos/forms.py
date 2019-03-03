from django.forms import ModelForm
from .models import UserInput

class UserInputForm(ModelForm):
    class Meta:
        model = UserInput
        exclude = ()  # this says to include all fields from model to the form
        #fields = ('customer', 'price', 'model')  # this would only display 3 fields on the form
