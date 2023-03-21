from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    start_date = models.DateField(
        blank=True,
        null=False,
        verbose_name="Дата начало"
    )
    finish_date = models.DateField(
        blank=True,
        null=False,
        verbose_name="Дата окончания"
    )
    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="Название")
    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Описание")
    user = models.ManyToManyField(User)