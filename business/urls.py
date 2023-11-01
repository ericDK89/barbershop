from django.urls import path
from . import views

urlpatterns = [
    path('', views.business, name='business'),
    path('admin_cancel_schedule/<int:schedule_id>', views.admin_cancel_schedule, name='admin_cancel_schedule'),
]
