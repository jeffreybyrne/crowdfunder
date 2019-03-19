from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import datetime

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    funding_goal = models.IntegerField(validators=[MinValueValidator(1)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects', default=1)

    def __str__(self):
        return self.title

    def total_pledged(self):
        total_purchased = 0
        for tier in self.reward_tiers.all():
            total_purchased += (tier.tier_value * len(tier.purchases.all()))
        return total_purchased


class RewardTier(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tier_value = models.IntegerField()
    total_rewards = models.IntegerField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reward_tiers')

    def __str__(self):
        return self.title


class Purchase(models.Model):
    backer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    reward_tier = models.ForeignKey(RewardTier, on_delete=models.CASCADE, related_name='purchases')
