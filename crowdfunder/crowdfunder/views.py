from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from crowdfunder.models import Project, RewardTier, Purchase


def home_page(request):
    context = {'projects': Project.objects.all() }
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def project_page(request, id):
    pass
