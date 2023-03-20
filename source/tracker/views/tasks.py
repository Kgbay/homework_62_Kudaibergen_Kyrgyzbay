from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from tracker.forms import TaskForm
from tracker.models import Task


class TaskDetail(DetailView):
    template_name = 'task.html'
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task_create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(LoginRequiredMixin,UpdateView,):
    template_name = 'task_update.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView,):
    template_name = 'task_confirm_remove.html'
    model = Task
    success_url = reverse_lazy('index')
