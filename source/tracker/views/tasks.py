from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from tracker.forms import TaskForm
from tracker.models import Task


class TaskDetail(DetailView):
    template_name = 'task.html'
    model = Task


class TaskCreateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'task_create.html'
    model = Task
    form_class = TaskForm
    success_message = 'Задача создана'
    permission_required = 'tracker.change_task'
    permission_denied_message = 'У вас не хватает прав доступа'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin,UpdateView,):
    template_name = 'task_update.html'
    form_class = TaskForm
    model = Task
    success_message = 'Задача обновлена'
    permission_required = 'tracker.change_task'
    permission_denied_message = 'У вас не хватает прав доступа'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView,):
    template_name = 'task_confirm_remove.html'
    model = Task
    success_url = reverse_lazy('index')
    permission_required = 'tracker.change_task'
    permission_denied_message = 'У вас не хватает прав доступа'
