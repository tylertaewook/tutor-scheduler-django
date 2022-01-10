from django import forms
from .models import Issue, Session


class IssuesForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. smitht24@kent-school.edu"})
    )

    class Meta:
        model = Issue
        fields = ["email", "issue", "user_agent"]


class SessionForm(forms.ModelForm):
    date = forms.DateField(disabled=True)
    # timeblock = forms.CharField(disabled=True)
    course_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. English 3"})
    )
    course_teacher = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. Mr. Kim"})
    )
    helptype = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "i.e. Term paper"})
    )

    class Meta:
        model = Session
        fields = ["date", "timeblock", "course_name", "course_teacher", "helptype"]
