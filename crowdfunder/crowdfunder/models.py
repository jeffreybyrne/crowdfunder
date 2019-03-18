from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    funding_goal = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')


class RewardTier(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tier_value = models.IntegerField()
    total_rewards = models.IntegerField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reward_tiers')


class Purchase(models.Model):
    backer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    reward_tier = models.ForeignKey(RewardTier, on_delete=models.CASCADE, related_name='purchases')
