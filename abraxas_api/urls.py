from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview_api, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
    path('task-status/<str:pk>/', views.taskStatus, name='task-status'),
    path('tasks/search', views.tasks, name='task-search')
  ]
