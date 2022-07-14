from django.conf.urls.static import static
from django.urls import path

from learning_log import settings

"""Определяет схемы URL для learning_logs."""

from .views import *


app_name = 'learning_logs'


urlpatterns = [
    path('', index, name='home'),
    path('topics/', topics, name='topics'),
    path('topics/<int:topic_id>/', topic, name='topic'),
    path('new_topic/', new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', edit_entry, name='edit_entry'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

