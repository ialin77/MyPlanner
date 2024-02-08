from django import forms
from .models import Plan


class CreatePlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['title', 'content', 'date', 'time']