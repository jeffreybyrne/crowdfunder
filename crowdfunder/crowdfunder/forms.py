
from django.forms import CharField, PasswordInput, ModelForm, Form
# from django.db import models
from crowdfunder.models import Project, RewardTier, Purchase
from datetime import datetime

class RewardTierForm(ModelForm):
    class Meta:
        model = RewardTier
        fields = ['title', 'description', 'tier_value', 'total_rewards', 'project']

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['backer', 'reward_tier']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'funding_goal']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_start_date = cleaned_data['start_date']
        cleaned_end_date = cleaned_data['end_date']

        if cleaned_start_date > cleaned_end_date:
            self.add_error('end_date', 'The end date must be after the start date')
        if cleaned_start_date < datetime.date(datetime.now()):
            self.add_error('start_date', 'The start date must be in the future')

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())
