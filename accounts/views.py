from django.views.generic import CreateView, TemplateView
from django.views import View
from django.contrib.auth.views import LoginView as DefaultLoginView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import Group

from django.shortcuts import render, redirect


class HomePageView(TemplateView):
    pass


class RegistrationView(View):
    form_class = RegistrationForm
    success_url = '/accounts/login'
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        account_type = request.POST.get('account_type')
        group_organiser = Group.objects.get(name='organisers')
        group_participant = Group.objects.get(name='participants')

        if form.is_valid():
            account_type = request.POST.get('account_type')

            user = form.save()
            print(user, account_type)
            if account_type.lower() == 'organiser':
                print("Added to organiser group")
                user.groups.add(group_organiser)
                user.is_organiser = True
            elif account_type.lower() == 'participant':
                print("added to participant group")
                user.groups.add(group_participant)
                user.is_participant = True

            user.save()
        return redirect(self.success_url)

class LoginView(DefaultLoginView):
    form_class  = LoginForm
    # template_name = 'registration/login.html'
