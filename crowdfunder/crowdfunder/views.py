from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from crowdfunder.models import Project
from crowdfunder.forms import ProjectForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home_page(request):
    context = {'projects': Project.objects.all() }
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def project_page(request, id):
    project = Project.objects.get(pk=id)
    context = {'project': project}
    response = render(request, 'project.html', context)
    return HttpResponse(response)


@login_required
def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save()
            new_project.owner = request.user
            new_project.save()
            return HttpResponseRedirect('/project/{}'.format(new_project.id))
    else:
        form = ProjectForm()
        context = {'form': form}
        print(context)
    return render(request, 'create_page.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/projects')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()

    context = {'form': form}
    response = render(request, 'login.html', context)
    return HttpResponse(response)
