from django import forms
from django.forms import widgets

from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["name"]
        widgets = {
            "name": widgets.Textarea(attrs={"placeholder": "Введите вопрос"})
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["name"]
        widgets = {
            "types": widgets.CheckboxSelectMultiple,
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["choice"]