from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from crowdfunder.models import Project, RewardTier, Purchase
from crowdfunder.forms import RewardTierForm, PurchaseForm


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
    reward = RewardTier.objects.get(pk=id)
    project = reward.project
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

def purchase_reward(request):
    if request.method == "POST":
        post_data = request.POST
        form = PurchaseForm(post_data)
        if form.is_valid():
            form.user = request.user
            new_purchase = form.save()
            return HttpResponseRedirect('/home')
            #This needs to be changed to a page that displays the users' purchases i.e. user home page
        else:
            pass
    else:
        form = PurchaseForm()
        context = {"form": form}
        response = render(request, 'purchase_reward.html', context)
        return HttpResponse(response)
