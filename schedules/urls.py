from django.urls import path
from . import views

urlpatterns = [
    path("seus_agendamentos", views.schedules, name="schedules")
]
