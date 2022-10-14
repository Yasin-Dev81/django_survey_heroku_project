from django.forms import ModelForm
from . import models


class NewSurveyTitleForm(ModelForm):
    class Meta:
        model = models.SurveyTitle
        fields = [
            'title_text',
            'description',
        ]


class NewSurveyQuestionForm(ModelForm):
    class Meta:
        model = models.SurveyQuestion
        fields = [
            'question_text',
        ]

    def __init__(self, title):
        super(NewSurveyQuestionForm, self).__init__()
        self.title = title
