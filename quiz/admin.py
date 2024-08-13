from django.contrib import admin
from .models import Question, PersonalityType, CareerQuestion, TopicScore

admin.site.register(Question)
admin.site.register(PersonalityType)
admin.site.register(CareerQuestion)
admin.site.register(TopicScore)
