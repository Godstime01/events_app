
from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.CreateEventView.as_view(), name='create_event'),
    path("list/", views.ListAllEvent.as_view(), name="events_list"),
    path("dashboard/", views.DashboardView.as_view(), name='dashboard'),
    path("register/<id>/", views.ParticipationView, name='participate'),
    path("", views.HomePageView.as_view(), name='index')
]