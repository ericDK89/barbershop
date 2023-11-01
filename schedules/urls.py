from django.urls import path
from . import views

urlpatterns = [
    path("seus_agendamentos", views.schedules, name="schedules"),
    path("novo_agendamento", views.new_schedule, name="new_schedule"),
    path("cancel_schedule/<int:schedule_id>", views.cancel_schedule, name="cancel_schedule"),
]
