from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

# for polls
from django.http import Http404
from django.http import HttpResponse

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"
