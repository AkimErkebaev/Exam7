from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView

from webapp.forms import ChoiceForm, AnswerForm
from webapp.models import Choice, Poll, Answer


class IndexViewAnswer(TemplateView):
    template_name = "answer/index.html"

    def get_context_data(self, **kwargs):
        answers = Answer.objects.order_by("-created_at")
        kwargs["answers"] = answers
        return super().get_context_data(**kwargs)


class CreateViewAnswer(CreateView):
    form_class = AnswerForm
    template_name = "answer/create.html"

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        form.instance.poll = poll
        print(form.instance)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})
