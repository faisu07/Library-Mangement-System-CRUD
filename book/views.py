from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    CreateView, 
    ListView, 
    UpdateView, 
    DetailView, 
    DeleteView
)

from django.urls import reverse_lazy

class BookDeleteView(DeleteView):
    model = Book
    template_name = "book/book_delete.html"
    success_url = reverse_lazy('book_list')
class BookListView(ListView):
    model = Book
    template_name = "book/library.html"
    context_object_name = "books"
class BookDetailView(DetailView):
    model = Book
    template_name = "book/book_detail.html"
    context_object_name = "books"
class BookUpdateView(UpdateView):
	model = Book
	fields = ('name','author','picture', 'describe','NumberOfCopies','Price','email','Discount','Release',)
	template_name = "book/upload_form.html"
	success_url = reverse_lazy('book_list')
class BookCreateView(CreateView):
    model = Book
    fields = ('name','author','picture','describe','NumberOfCopies','Price','email','Discount','Release',)
    template_name = "book/upload_form.html"
    success_url = reverse_lazy('book_list')
