import threading
from . import models


class SaveSurvey(threading.Thread):
    def __init__(self, data, question_len, option_len, author):
        super(SaveSurvey, self).__init__()
        self.database_title = None
        self.description = ''
        self.title = ''
        self.data = data
        self.question_len = question_len
        self.option_len = option_len
        self.survey_data = {}
        self.author = author

    def set_title(self):
        self.title = self.data.get('survey_title')[0]
        self.description = self.data.get('survey_description')[0]
        print('---title:', self.title, '\n---description:', self.description)
        # save to database code
        self.database_title = models.SurveyTitle.objects.create(
            title_text=self.title,
            description=self.description,
            author=self.author
        )

    def set_questions(self):
        for i in range(1, self.question_len + 1):
            self.survey_data[i] = {
                'question': self.data.get('survey_question_%s' % i)[0],
                'options': []
            }

    def set_options(self):
        for i in range(1, self.option_len + 1):
            z = 1
            for j in self.data.get('survey_option_%s' % i):
                print(j)
                self.survey_data[z]['options'].append(j)
                z += 1

    def save_to_database(self):
        for i in self.survey_data:
            i = self.survey_data[i]
            if i['question'] == '':
                print('not valid question text')
            else:
                database_question = models.SurveyQuestion.objects.create(
                    question_text=i['question'],
                    title=self.database_title,
                )
                for j in i['options']:
                    if j == '':
                        print('not valid option text')
                    else:
                        models.SurveyOption.objects.create(
                            option_text=j,
                            question=database_question
                        )

    def run(self) -> None:
        self.set_title()
        self.set_questions()
        self.set_options()
        print(self.survey_data)
        self.save_to_database()
