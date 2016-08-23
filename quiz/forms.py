from django import forms
from .models import Post

class AnswersForm(forms.ModelForm):

    class Meta:
        model = Answers
        fields = ['answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8', 'answer9', 'answer10']