from django.shortcuts import render, redirect
from .models import Login
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class CustomLoginView(LoginView):
    model = Login
    template_name = 'user_auth/login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        # Redirect to 'logged_in' page after login
        return reverse_lazy('logged_in')  # Redirect to the custom 'logged_in' URL

class RegisterPage(FormView):
    template_name = 'user_auth/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('login')
        return super(RegisterPage, self).get(*args, **kwargs)
    
class LoggedInView(TemplateView):
    template_name = 'user_auth/logged_in.html'