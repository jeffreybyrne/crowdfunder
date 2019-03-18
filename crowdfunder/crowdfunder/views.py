from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from crowdfunder.models import Project, RewardTier, Purchase
from crowdfunder.forms import RewardTierForm


def home_page(request):
    context = {'projects': Project.objects.all() }
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def project_page(request, id):
    pass

def reward_page(request, id):
    pass

def rewards(request, id):
    project = Project.objects.get(pk=id)
    rewards = project.reward_tiers.all()
    owner = project.owner
    context = {'rewards': rewards, 'owner': owner}
    response = render(request, 'rewards.html', context)
    return HttpResponse(response)

def edit_reward(request, id):
    project = Project.objects.get(pk=id)
    reward = RewardTier.objects.get(pk=id)
    if request.method == 'GET':
        form = RewardTierForm(instance=reward)
        context = {'reward': reward, 'form': form }
        response = render(request, 'edit_reward.html', context)
        return HttpResponse(response)
    elif request.method == 'POST':
        form = RewardTierForm(request.POST, instance=reward)
        if form.is_valid():
            edited_reward = form.save()
            return HttpResponseRedirect('/project/{}/rewards/'.format(project.id))
        else:
            context = {'form': form, 'reward': reward }
            response = render(request, 'edit_reward.html', context)
            return HttpResponse(response)
