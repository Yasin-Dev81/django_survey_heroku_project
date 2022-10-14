from django.urls import path, include
from . import views


urlpatterns = [
    path('list/', views.SurveyListView.as_view(), name='survey_list_url'),
    path('detail/statistics/<int:title_pk>/', views.survey_statistics_view, name='survey_statistics_url'),
    path('detail/surveying/<int:title_pk>/', views.surveying_view, name='surveying_url'),
    path('create/<int:question_len>/<int:option_len>/', views.creat_survey_view, name='survey_create_with_num_url'),
    path('create/#/', views.select_num_for_creat_survey_view, name='survey_create_without_num_url')
]
