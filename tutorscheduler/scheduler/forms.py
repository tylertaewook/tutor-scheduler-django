from django import forms
from .models import Issue, Session


class IssuesForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. smitht24@kent-school.edu"})
    )

    class Meta:
        model = Issue
        fields = ["email", "issue", "user_agent"]
