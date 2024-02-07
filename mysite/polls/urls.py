from django.urls import path

from . import views
from .views import add_reply, removePoll, search_results

urlpatterns = [
    path("", views.home, name="home"),
    path('create-poll/', views.create_poll, name="create_poll"),
    path("remove-poll/", views.remove_poll, name="removePoll"),
    path("poll/<int:poll_id>/", views.poll_detail, name="poll_detail"),
    path('poll/<int:poll_id>/add_reply/', add_reply, name='add_reply'),
    path('poll/remove/<int:poll_id>/', removePoll, name='remove_poll'),
    path('poll/search/', search_results, name='search_results')
]
