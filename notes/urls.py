from django.urls import re_path, path

from notes.views import NoteDetailView, NoteListView

urlpatterns = [
    re_path(r'^$', NoteListView.as_view(), name='note-list'),
    re_path(r'^(?P<pk>\d+)/$', NoteDetailView.as_view(), name='note-detail'),
]