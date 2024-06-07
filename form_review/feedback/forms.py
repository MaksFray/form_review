from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20, min_length=4, error_messages={
        'max_length': "Too much symbols",
        'min_length': "Not enough symbols",
    })
    second_name = forms.CharField()
    rating = forms.IntegerField(label='Rating', max_value=5, min_value=1)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
