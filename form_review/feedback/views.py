from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        second_name = request.POST['second_name']
        feedback = request.POST['feedback']
        return HttpResponseRedirect('/done')
    return render(request, 'feedback/feedback.html')

def done(request):
    return render(request, 'feedback/done.html')