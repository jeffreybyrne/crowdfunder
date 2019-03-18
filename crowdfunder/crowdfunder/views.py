from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from crowdfunder.models import Project, RewardTier, Purchase


def home_page(request):
    context = {'projects': Project.objects.all() }
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def project_page(request, id):
    pass

def reward_page(request, id):
    pass
    # reward = RewardTier.objects.get(pk = id)
    # context = {'reward': reward}
    # response = render(request, 'rewards.html', context)
    # return HttpResponse(response)

def rewards(request, id):
    project = Project.objects.get(pk=id)
    rewards = project.reward_tiers.all()
    context = {'rewards': rewards}
    response = render(request, 'rewards.html', context)
    return HttpResponse(response)
