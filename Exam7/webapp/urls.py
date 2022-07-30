from django.urls import path

from webapp.views import IndexView, CreatePoll, PollView, UpdatePoll, DeletePoll, IndexViewChoice, CreateChoice, \
    UpdateChoice, DeleteChoice, IndexViewAnswer, CreateViewAnswer


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('polls/create/', CreatePoll.as_view(), name="create_poll"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    path('poll/<int:pk>/update', UpdatePoll.as_view(), name="update_poll"),
    path('poll/<int:pk>/delete', DeletePoll.as_view(), name="delete_poll"),
    path('choice/', IndexViewChoice.as_view(), name="index_choices"),
    path('poll/<int:pk>/choice/add/', CreateChoice.as_view(), name="create_choice"),
    path('choice/<int:pk>/update', UpdateChoice.as_view(), name="update_choice"),
    path('choice/<int:pk>/delete', DeleteChoice.as_view(), name="delete_choice"),
    path('poll/<int:pk>/answer/add/', CreateViewAnswer.as_view(), name="create_answers"),
    path('answers/', IndexViewAnswer.as_view(), name="index_answers"),
]
