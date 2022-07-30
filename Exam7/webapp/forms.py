from django import forms
from django.forms import widgets

from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["name"]
        widgets = {
            "name": widgets.Textarea(attrs={"placeholder": "Введите вопрос"})
        }


