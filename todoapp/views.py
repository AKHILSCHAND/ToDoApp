from django.shortcuts import get_object_or_404, redirect, render

from todoapp.models import Task

# Create your views here.


def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def mark_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


