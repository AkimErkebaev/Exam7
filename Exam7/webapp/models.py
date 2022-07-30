from django.db import models
from django.urls import reverse


class Poll(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.id}. {self.name}"

    def get_absolute_url(self):
        return reverse("poll_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "polls"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Choice(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False, verbose_name="Название")
    poll = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE, related_name="choices",
                               verbose_name='Вопрос')

    def __str__(self):
        return f"{self.id}. {self.name}"

    class Meta:
        db_table = "choices"
        verbose_name = "Выбор"
        verbose_name_plural = "Выборы"


class Answer(models.Model):
    poll = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE, related_name="answerspoll",
                               verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    choice = models.ForeignKey("webapp.Choice", on_delete=models.CASCADE, related_name="answerschoice",
                                verbose_name='Ответ')

    def __str__(self):
        return f"{self.id}. {self.poll}: {self.choice}"

    class Meta:
        db_table = "answers"
        verbose_name = "Ответы"
        verbose_name_plural = "Ответ"