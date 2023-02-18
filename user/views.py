from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')
    template_name = 'registration/register.html'

    def get_success_url(self):
        if not self.success_url:
            raise ImproperlyConfigured('No URL to redirect to. Provide a success url.')
        return str(self.success_url)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

class PasswordChangeForm(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')
    template_name = 'registration/password_change.html'

    def get_success_url(self):
        if not self.success_url:
            raise ImproperlyConfigured('No URL to redirect to. Provide a success url.')
        return str(self.success_url)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)