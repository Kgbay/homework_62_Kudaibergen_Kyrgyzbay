from django.views.generic import ListView, CreateView

from tracker.models import Project


class ProjectView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'



