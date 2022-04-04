from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-input'}),
            'content': forms.Textarea(attrs={"cols": 60, "rows": 10})
        }

    def clean_video_url(self):
        video_url = self.cleaned_data['video_url']
        if not video_url.strip().startswith('https://youtu.be/'):
            raise ValidationError("Вставьте короткую ссылку из YouTube. Она начинается на https://youtu.be/")
        return video_url.strip()