from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.

def index(request):

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feed = Feedback(
                name = form.cleaned_data['name'],
                second_name = form.cleaned_data['second_name'],
                rating = form.cleaned_data['rating'],
                feedback = form.cleaned_data['feedback']
            )
            feed.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})

def done(request):
    return render(request, 'feedback/done.html')