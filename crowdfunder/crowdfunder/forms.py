from django.forms import CharField, PasswordInput, ModelForm
# from django.db import models
from django import forms
from crowdfunder.models import Project, RewardTier, Purchase

class RewardTierForm(ModelForm):
    class Meta:
        model = RewardTier
        fields = ['title', 'description', 'tier_value', 'total_rewards', 'project']
