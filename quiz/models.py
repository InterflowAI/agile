
# Create your models here.
from django.db import models

class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class PersonalityType(models.Model):
    code = models.CharField(max_length=5, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.code
class CareerQuestion(models.Model):
    topic = models.CharField(max_length=50)
    question = models.TextField()
    options = models.TextField()
    answer = models.CharField(max_length=50)

class TopicScore(models.Model):
    topic = models.CharField(max_length=50)
    score = models.IntegerField(default=0)