from django.views.generic import ListView, DetailView

from notes.models import Note

class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note