from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse

from notes.forms import CustomUserCreationForm
from notes.models import Note, Topic


class TopicListView(LoginRequiredMixin, ListView):
    model = Topic


class TopicDetailView(DetailView):
    model = Topic


class TopicCreate(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'parent', 'is_public']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TopicCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('topic-list')


class TopicUpdate(LoginRequiredMixin, UpdateView):
    model = Topic
    fields = ['title', 'parent', 'is_public']

    def get_success_url(self):
        return reverse('topic-list')

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        current_topic = self.get_object()
        if not (current_topic.author == request.user):
            raise PermissionDenied
        return handler


class TopicDelete(LoginRequiredMixin, DeleteView):
    model = Topic

    def get_success_url(self):
        return reverse('topic-list')

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        current_topic = self.get_object()
        if not (current_topic.author == request.user):
            raise PermissionDenied
        return handler


class NoteListView(LoginRequiredMixin, ListView):
    model = Note

    def get_queryset(self):
        return Note.objects.filter(
            author=self.request.user
        )#.order_by('-date_posted') #TODO add field of created_date to note model and use it in ordering notes


class NoteDetailView(DetailView):
    model = Note


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NoteCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('note-list')


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'body']

    def get_success_url(self):
        return reverse('note-list')

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        current_note = self.get_object()
        if not (current_note.author == request.user):
            raise PermissionDenied
        return handler


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

    def get_success_url(self):
        return reverse('note-list')

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        current_note = self.get_object()
        if not (current_note.author == request.user or request.user.is_superuser):
            raise PermissionDenied
        return handler


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