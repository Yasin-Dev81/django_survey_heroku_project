from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from . import models, forms, tasks


# finished
class SurveyListView(generic.ListView):
    template_name = 'survey/survey_list.html'
    model = models.SurveyTitle
    context_object_name = 'survey_list'


# finished
@login_required
def surveying_view(request, title_pk):
    question_list = get_object_or_404(models.SurveyTitle, pk=title_pk).survey_question_list.all()
    page = request.GET.get('page', 1)

    paginate_by = 1
    paginator = Paginator(question_list, paginate_by)

    try:
        values = paginator.page(page)
    except PageNotAnInteger:
        values = paginator.page(1)
    except EmptyPage:
        values = paginator.page(paginator.num_pages)

    if request.method == "POST":
        print(request.POST)
        if request.POST.get('answer') != 'blank':
            models.SurveyAnswer.objects.create(
                author=request.user,
                option_id=request.POST.get('answer')
            )
            print('--- answer added.')
        if request.POST.get('input_next') == 'Finish':
            print('finished')
            return redirect(reverse('survey_statistics_url', args=[title_pk, ]))
    else:
        pass
    return render(
        request=request,
        template_name='survey/surveying.html',
        context={
            'question': values.object_list[0],
            'values': values,
            'question_list': question_list
        }
    )


# finished
def survey_statistics_view(request, title_pk):
    return render(
        request,
        'survey/survey_statistics.html',
        context={
            'statics': get_object_or_404(models.SurveyTitle, pk=title_pk).survey_question_list.all()
        }
    )


# finished
@login_required
def creat_survey_view(request, question_len, option_len):
    if request.method == 'POST':
        data = dict(request.POST)
        del data['csrfmiddlewaretoken']
        print(data)
        if data.get('survey_title')[0] == '':
            return HttpResponse('title is not entered!')
        else:
            cl = tasks.SaveSurvey(data, question_len, option_len, request.user)
            cl.run()
            return redirect(reverse('survey_statistics_url', args=[cl.database_title.pk]))
    else:
        pass
    return render(
        request=request,
        template_name='survey/survey_question_create.html',
        context={
            'question_len': range(1, question_len+1),
            'option_len': range(1, option_len+1),
        }
    )


# finished
@login_required
def select_num_for_creat_survey_view(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect(
            reverse(
                'survey_create_with_num_url',
                args=[
                    int(request.POST.get('question_len')[0]),
                    int(request.POST.get('option_len')[0])
                ]
            )
        )
    return render(
        request,
        template_name='survey/survey_select_num.html'
    )
