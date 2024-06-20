from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import GalleryUploadForm
from .models import Gallery

class ListGallery(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'images'

class CreateGalleryView(CreateView):
    model = Gallery
    # fields = '__all__'
    form_class = GalleryUploadForm
    template_name = 'gallery/load_file.html'
    success_url = 'load_image'
