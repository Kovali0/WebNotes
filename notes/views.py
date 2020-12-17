from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse

from notes.forms import CustomUserCreationForm
from notes.models import Note

class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note

class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'body']

class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'body']

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

def Dashboard(request):
    return render(request, "users/dashboard.html")

def Register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))