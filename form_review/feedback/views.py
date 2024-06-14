from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

# Create your views here.
class FeedBackView(CreateView):
    model = Feedback
    # fields = '__all__'
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivan'
        context['date'] = '20.02.20'
        return context

class AllFeedbacksView(ListView):
    template_name = 'feedback/feedback_list.html'
    model = Feedback
    context_object_name = 'feedbacks'
    def get_queryset(self):
        queryset = super().get_queryset()
        # filter_gs = queryset.filter(rating__gt=3)
        return queryset

class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback

class FeedBackUpdateView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})
    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        return render(request, 'feedback/feedback.html', context={'form': form})