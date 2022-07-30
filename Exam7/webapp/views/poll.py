from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm
from webapp.models import Poll


class IndexView(ListView):
    model = Poll
    template_name = "polls/index.html"
    context_object_name = "polls"
    ordering = "-created_at"
    paginate_by = 5


class PollView(DetailView):
    template_name = "polls/poll_view.html"
    model = Poll
    context_object_name = "polls"


class CreatePoll(CreateView):
    form_class = PollForm
    template_name = "polls/create.html"

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        form.save_m2m()
        return redirect("poll_view", pk=project.pk)


class UpdatePoll(UpdateView):
    form_class = PollForm
    template_name = "polls/update.html"
    model = Poll


class DeletePoll(DeleteView):
    model = Poll
    template_name = "polls/delete.html"
    success_url = reverse_lazy('index')