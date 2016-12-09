from django.views.generic import ListView

from question_and_answer.models import QuestionAndAnswer


class QAListView(ListView):
    model = QuestionAndAnswer
    template_name = 'question_and_answer/qa_list.html'

    def get_queryset(self):
        queryset_objs = QuestionAndAnswer.objects.filter(enabled=True)
        dict_return = {}
        for q_obj in queryset_objs:
            dict_return[q_obj.answer] = q_obj.question
        return dict_return

