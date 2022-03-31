"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from mirai import views
from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings 
from django.conf.urls.static import static 
from mirai.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #Company paths 
    path('comp', views.comp),
    path('show', views.show),
    path('edit/<str:cName>', views.edit),
    path('update/<str:cName>', views.update),
    path('delete/<str:cName>', views.delete), 

    #employee paths
    path('emp', views.emp),
    path('showemp', views.showemp),
    path('deleteEmp/<str:eFname>', views.deleteEmp),
    path('editemp/<str:eFname>', views.editemp), 
    path('updateEmp/<str:eFname>', views.updateEmp),
    path('filter_emp', views.filter_emp),




    path('export/', views.export),
    path('', views.simple_upload),

    path('task', views.task),
    path('showtask/', views.showtask),
    path('task/add_task/<str:eFname>', views.add_task, name='task'),
    # path('task/add_task/', views.add_task, name='add_task'),
    # path('<int:task_id>/remove_task/', views.remove_task, name='remove_task'),
    # path('<int:goal_id>/remove_goal/', views.remove_goal, name='remove_goal'),
    # path('<int:task_id>/add_task_to_daily_tasks/', views.add_task_to_daily_tasks, name='add_task_to_daily_tasks'),
    # path('<int:task_id>/remove_task_from_daily_tasks/', views.remove_task_from_daily_tasks, name='remove_task_from_daily_tasks'),
    path('task/add_goal/<str:eFname>', views.add_goal, name='add_goal'),
    # path('<int:task_id>/task_done/', views.task_done, name='task_done'),
    # path('history/', views.history, name='history'),
    # path('tasks_list/', views.TaskListView.as_view(), name='tasks_list'),
    # path('signup_page/', views.SignUpPage.as_view(), name='signup_page'),
    # path('<int:task_id>/remove_task/', views.remove_task, name='remove_task'),
    #Homepage path
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    #inbuilt login path
    path('accounts/', include('django.contrib.auth.urls')),
]
#for Media Storage 
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 