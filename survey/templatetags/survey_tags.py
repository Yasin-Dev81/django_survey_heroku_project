from django import template

register = template.Library()


@register.filter
def num_to_percent(num, all_database):
    total_num = 0
    for i in all_database:
        total_num += i.survey_answer_list.count()
    if total_num == 0:
        return 0
    return (num/total_num) * 100
