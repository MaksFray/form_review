from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'second_name', 'feedback', 'rating']
        fields = '__all__'
        # exclude = ['name']
        labels = {
            'name': 'Name',
            'second_name': 'Second name',
            'rating': 'Rating',
            'feedback': 'Feedback',
        }
        error_messages = {
            'name':{
                'max_length': 'Too many symbols',
                'min_length': 'Too few symbols',
                'required': 'Must not be empty',
            },
            'second_name': {
                'max_length': 'Too many symbols',
                'min_length': 'Too few symbols',
                'required': 'Must not be empty',
            }
        }