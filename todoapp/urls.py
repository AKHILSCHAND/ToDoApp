from django.urls import path

from . import views

urlpatterns = [
    path('add_task', views.add_task, name='add_task'),
    path('mark_done/<int:pk>', views.mark_done, name='mark_done'),
    path('mark_undone/<int:pk>', views.mark_undone, name='mark_undone'),
    
    
]