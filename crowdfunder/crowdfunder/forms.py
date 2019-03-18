from django import forms
from crowdfunder.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'funding_goal']


class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
