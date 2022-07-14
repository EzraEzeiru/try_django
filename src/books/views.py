from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from .models import Books
from .forms import AddForm

# Create your views here.


class IndexView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_set = Books.objects.all()
        context = {
            "object_list": query_set
        }

        return context


class BookDetailView(DetailView):
    model = Books
    template_name = "books_detail.html"
    context_object_name = "book"


class GenreView(ListView):
    model = Books
    template_name = "home.html"
    context_object_name = "object_list"

    def get_queryset(self, *args, **kwargs):
        return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))


class AddBookView(FormView):
    template_name = "add.html"
    form_class = AddForm
    success_url = "/books/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BookEditView(UpdateView):
    model = Books
    form_class = AddForm
    template_name = "add.html"
    success_url = "/books/"


class BookDeleteView (DeleteView):
    model = Books
    template_name = "delete.html"
    context_object_name = "book"
    success_url = "/books/"
