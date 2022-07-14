from django.shortcuts import render
from .models import Post
from django.views.generic.base import TemplateView


# Create your views here.
class Ex2View(TemplateView):
    template_name = "ex2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "post": Post.objects.get(id=1),
            'data': "Context Data for Ex2"
        }
        return context