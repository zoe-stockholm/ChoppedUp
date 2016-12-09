import json

from django.http import HttpResponse
from django.views.generic import ListView

from question_and_answer.models import QuestionAndAnswer


class QAListView(ListView):
    model = QuestionAndAnswer
    template_name = 'question_and_answer/qa_list.html'
    queryset = QuestionAndAnswer.objects.filter(enabled=True)

    def get(self, request, *args, **kwargs):
        dict_return = {}
        for obj in self.queryset:
            dict_return.update(obj.to_dict())
        return HttpResponse(
            json.dumps({"data": dict_return}),
            content_type='application/json')


