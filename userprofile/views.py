from django.http import Http404,HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
# from django.views.generic import View, ListView, DetailView
from django.shortcuts import render

from account.models import User
from .models import Profile

@login_required
def user_profile(request):
    if request.user.is_staff:
        qs = Profile.objects.all()
        context = {
        "query_set" : qs
        }
        template ="profile/user_profile.html"
        return render(request, template, context)

    else:
        qs = Profile.objects.get(user= request.user)
        context = {
        "query_set" : qs
        }
        template ="profile/user_profile.html"
        return render(request, template, context)
