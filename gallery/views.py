from django.shortcuts import render
from .models import Gallery
# Create your views here.
def home(request):
    gallerys = Gallery.objects
    return render(request, 'home.html', {'gallerys': gallerys})
