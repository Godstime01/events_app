
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages

from .forms import EventCreationForm, ParticipationForm
from .models import Event, ParticipationModel

from django.shortcuts import render, redirect


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Event.objects.all()[5:]
        context['events'] = events
        return context


class CreateEventView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = EventCreationForm
    template_name = 'event_create.html'
    success_url = '/'
    login_url = 'login'

    def form_valid(self, form):
        print(form)
        form.instance.organiser = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        # Check if the user is in the specified group
        return self.request.user.groups.filter(name='organisers').exists()
    

class ListAllEvent(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event_list.html'


class DashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView ):
    model = Event
    template_name = 'dashboard.html'
    paginate_by = 5
    context_object_name ='events'

    # def get_context_data(self, *args, **kwargs):

    #     return context

    def get_queryset(self):

        queryset = super().get_queryset()
        eventQuery = Event.objects.filter(organiser = self.request.user)
        
        return eventQuery

    def get_context_data(self, **kwargs):

        domain = self.request.get_host()
        print(domain)
        context = super().get_context_data(**kwargs)
        eventQuery = Event.objects.filter(organiser = self.request.user)
        # participantQuery = ParticipationModel.objects.filter()
        # context['events'] = eventQuery
        return context
    
    
    

    def test_func(self):
    # Check if the user is in the specified group
        return self.request.user
    
def ParticipationView(request, id):
    event = Event.objects.get(id = id)

    form = ParticipationForm()

    if request.method == 'POST':
        form = ParticipationForm(request.POST)

        if form.is_valid():
            try:
                ev = form.save(commit=False)
                ev.event = event
                ev.save()
                return redirect("/")
            except ValueError as e:
                messages.info(request, 'Max participant reached')
                return render(request, 'participate.html', {'form': form, 'event': event}) 
        
    

    

    return render(request, 'participate.html', {'form': form, 'event': event})
