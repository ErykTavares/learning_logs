from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """classe que representa o formulario de Topic"""
    class Meta():
        model = Topic
        fields = ["text"]
        labels = {"text": ''}


class EntryForm(forms.ModelForm):
    """classe que representa o formulario de Entry"""
    class Meta():
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}