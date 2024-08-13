'''from django import forms
from .models import Question
from django import forms
from .models import CareerQuestion

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[('1', 'Option 1'), ('2', 'Option 2')],
                widget=forms.RadioSelect
            )


class CareerQuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CareerQuizForm, self).__init__(*args, **kwargs)
        questions = CareerQuestion.objects.all()
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')],
                widget=forms.RadioSelect,
                label=question.text
            )
'''
from django import forms
from .models import Question, CareerQuestion

class QuizForm(forms.Form):
    from django import forms

from django import forms
from .models import Question


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.IntegerField(
                widget=forms.HiddenInput(),
                initial=1,  # default to option 1
                label=question.text
            )




class CareerQuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CareerQuizForm, self).__init__(*args, **kwargs)
        questions = CareerQuestion.objects.all()
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')],
                widget=forms.RadioSelect,
                label=question.text
            )
