from django.contrib import admin

from question_and_answer.models import QuestionAndAnswer, Topic


class QuestionAndAnswersInline(admin.TabularInline):
    model = QuestionAndAnswer
    extra = 0


class QuestionAndAnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'updated', 'created', 'topic', 'enabled']
    list_filter = ['enabled', 'topic']
    search_fields = ['answer']
    actions = ['mark_as_enable', 'mark_as_disable']

    def mark_as_enable(self, request, queryset):
        queryset.update(enabled=True)

    def mark_as_disable(self, request, queryset):
        queryset.update(enabled=False)

    mark_as_enable.short_description = "Mark selected items as enable"
    mark_as_disable.short_description = "Mark selected items as disable"


class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic']
    search_fields = ['topic']

    inlines = [QuestionAndAnswersInline]


admin.site.register(QuestionAndAnswer, QuestionAndAnswerAdmin)
admin.site.register(Topic, TopicAdmin)
