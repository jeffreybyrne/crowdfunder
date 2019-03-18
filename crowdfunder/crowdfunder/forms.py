
from django.forms import CharField, PasswordInput, ModelForm, Form
# from django.db import models
from crowdfunder.models import Project, RewardTier, Purchase

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

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())
