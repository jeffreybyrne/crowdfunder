"""crowdfunder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crowdfunder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page, name = 'home_page'),
    path('project/<int:id>', views.project_page, name = 'project_page'),
    # path('reward/<int:id>', views.reward_page, name = 'reward_page'),
    path('project/<int:id>/rewards/', views.rewards, name = 'rewards'),
    path('edit_reward/<int:id>', views.edit_reward, name = 'edit_reward'),
    path('purchase_reward/<int:id>', views.purchase_reward, name = 'purchase_reward'),
    path('project/new', views.new_project, name='new_project_page'),
    path('login/', views.login_view, name='login'),
    path('project/<int:id>/add_rewards', views.add_rewards, name='add_rewards')

]
