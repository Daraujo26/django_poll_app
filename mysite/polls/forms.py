from django import forms
from .models import Question, Response

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['response_text']