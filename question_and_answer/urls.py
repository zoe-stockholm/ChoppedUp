from django.conf.urls import url

from question_and_answer.views import QAListView

app_name = 'question_and_answer'
urlpatterns = [
    url(r'^$', QAListView.as_view(), name='qa-list'),]
