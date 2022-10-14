from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class SurveyTitle(models.Model):
    title_text = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='survey_title_list'
    )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[%s]%s" % (self.author, self.title_text)

    def get_absolute_url(self):
        return reverse('home_url')


class SurveyQuestion(models.Model):
    title = models.ForeignKey(
        SurveyTitle,
        on_delete=models.CASCADE,
        related_name='survey_question_list',
        blank=False,
        null=False
    )

    question_text = models.TextField(blank=False, null=False)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[%s]%s : %s" % (
            self.title.author,
            self.title.title_text,
            self.question_text
        )

    def get_absolute_url(self):
        return reverse('home_url')


class SurveyOption(models.Model):
    question = models.ForeignKey(
        SurveyQuestion,
        on_delete=models.CASCADE,
        related_name='survey_option_list',
        blank=False,
        null=False
    )

    option_text = models.TextField(blank=False, null=False)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.option_text

    def get_absolute_url(self):
        return reverse('home_url')


class SurveyAnswer(models.Model):
    option = models.ForeignKey(
        SurveyOption,
        on_delete=models.CASCADE,
        related_name='survey_answer_list',
        blank=False,
        null=False
    )

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='survey_answer_list'
    )

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[%s]%s : %s : %s[%s]" % (
            self.option.question.title.author,
            self.option.question.title.title_text,
            self.option.question.question_text,
            self.option.option_text,
            self.author
        )

    def get_absolute_url(self):
        return reverse('home_url')

