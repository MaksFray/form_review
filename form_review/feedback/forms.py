from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField()
    second_name = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
