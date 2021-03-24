from django.forms import ModelForm

from .models import Questions

class CreateQuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question']