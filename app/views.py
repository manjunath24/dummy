from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Institute
#commit

class InstituteCreateView(CreateView):
    model = Institute
    exclude = ['id']
    template_name = 'registration.html'
