from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django.utils.safestring import mark_safe

from workways.mixins import NextUrlMixin, RequestFormAttachMixin
from .forms import LoginForm, RegisterForm
from .models import GuestEmail


# @login_required # /accounts/login/?next=/some/path/
# def account_home_view(request):
#     return render(request, "accounts/home.html", {})


#LoginRequiredMixin,
class AccountHomeView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/home.html'
    def get_object(self):
        return self.request.user


class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'
    default_next = '/'

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'
