from django.urls import re_path, path

from notes.views import NoteDetailView, NoteListView, NoteCreate, NoteUpdate, NoteDelete, Dashboard, Register

urlpatterns = [
    re_path(r'^$', NoteListView.as_view(), name='note-list'),
    re_path(r'^(?P<pk>\d+)/$', NoteDetailView.as_view(), name='note-detail'),
    re_path(r'note/add/$', NoteCreate.as_view(), name='note-form'),
    re_path(r'note/(?P<pk>[0-9]+)/$', NoteUpdate.as_view(), name='note-update-form'),
    re_path(r'note/(?P<pk>[0-9]+)/delete/$', NoteDelete.as_view(), name='note-confirm-delete'),
    re_path(r'users/dashboard/', Dashboard, name='dashboard'),
    re_path(r'^register/', Register, name='register'),
]