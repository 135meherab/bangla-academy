from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.

class SignUpView(FormView):
    template_name = 'user_accounts/signup_form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoingView(LoginView):
    template_name = 'user_accounts/login_form.html'
    def get_success_url(self):
        return reverse_lazy('index')