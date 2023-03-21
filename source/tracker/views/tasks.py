from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from tracker.forms import TaskForm
from tracker.models import Task


class TaskDetail(DetailView):
    template_name = 'task.html'
    model = Task


class GroupPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name__in=['project_manager', 'team_lead', 'admin']).exists()


class TaskCreateView(GroupPermissionMixin, SuccessMessageMixin, CreateView):
    template_name = 'task_create.html'
    model = Task
    form_class = TaskForm
    success_message = 'Задача создана'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(GroupPermissionMixin, SuccessMessageMixin, UpdateView, ):
    template_name = 'task_update.html'
    form_class = TaskForm
    model = Task
    success_message = 'Задача обновлена'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(GroupPermissionMixin, SuccessMessageMixin, DeleteView, ):
    template_name = 'task_confirm_remove.html'
    model = Task
    success_url = reverse_lazy('index')
    success_message = 'Задача удалена'
