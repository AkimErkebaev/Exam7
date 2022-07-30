from django.urls import path

from webapp.views import IndexView, CreatePoll, PollView, UpdatePoll, DeletePoll

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('polls/create/', CreatePoll.as_view(), name="create_poll"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    path('poll/<int:pk>/update', UpdatePoll.as_view(), name="update_poll"),
    path('poll/<int:pk>/delete', DeletePoll.as_view(), name="delete_poll"),
]
