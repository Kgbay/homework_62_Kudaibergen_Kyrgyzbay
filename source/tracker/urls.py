from django.urls import path

from .views.base import IndexView
from .views.tasks import TaskCreateView, TaskDetail, TaskDeleteView, TaskUpdateView
from .views.projects import ProjectView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("task/add/", TaskCreateView.as_view(), name='task_add'),
    path("tasks/<int:pk>/", TaskDetail.as_view(), name='task_view'),
    path("tasks/<int:pk>/remove/", TaskDeleteView.as_view(), name='remove_task'),
    path("tasks/<int:pk>/confirm_remove/", TaskDeleteView.as_view(), name='confirm_remove_task'),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="update_task"),
    path("projects/", ProjectView.as_view(), name='project'),
]