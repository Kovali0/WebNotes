from django.urls import re_path, path

from notes.views import NoteDetailView, NoteListView, NoteCreate, NoteUpdate, NoteDelete, Dashboard, Register, \
    TopicListView, TopicDetailView, TopicCreate, TopicUpdate, TopicDelete

urlpatterns = [
    #re_path(r'', Dashboard, name='dashboard'),
    re_path(r'^$', NoteListView.as_view(), name='note-list'),
    re_path(r'^(?P<pk>\d+)/$', NoteDetailView.as_view(), name='note-detail'),
    re_path(r'note/add/$', NoteCreate.as_view(), name='note-form'),
    re_path(r'note/(?P<pk>[0-9]+)/$', NoteUpdate.as_view(), name='note-update-form'),
    re_path(r'note/(?P<pk>[0-9]+)/delete/$', NoteDelete.as_view(), name='note-confirm-delete'),
    re_path(r'users/dashboard/', Dashboard, name='dashboard'),
    re_path(r'^register/', Register, name='register'),
    re_path(r'topics/', TopicListView.as_view(), name='topic-list'),
    re_path(r'topics/(?P<pk>\d+)/$', TopicDetailView.as_view(), name='topic-detail'),
    re_path(r'topics/add/$', TopicCreate.as_view(), name='topic-form'),
    re_path(r'topics/(?P<pk>[0-9]+)/$', TopicUpdate.as_view(), name='topic-update-form'),
    re_path(r'topics/(?P<pk>[0-9]+)/delete/$', TopicDelete.as_view(), name='topic-confirm-delete'),
]