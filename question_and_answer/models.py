from django.db import models


class Topic(models.Model):
    topic = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['topic']

    def __str__(self):
        return self.topic


class QuestionAndAnswer(models.Model):
    answer = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, related_name='question_and_answer_topic')
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ['-updated', ]

    def __str__(self):
        return 'Q: {}. A: {}'.format(self.question, self.answer)

    def to_dict(self):
        return {self.answer: self.question}

