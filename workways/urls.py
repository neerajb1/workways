from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, RedirectView


from account.views import LoginView, RegisterView
from userprofile.views import (
    user_profile,
    )


urlpatterns = [
    url(r'^$', user_profile, name='profile'),
    url(r'^accounts/$', RedirectView.as_view(url='/account')),
    # url(r'^account/', include("account.urls", namespace='account')),
    # url(r'^accounts/', include("account.passwords.urls")),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^settings/$', RedirectView.as_view(url='/account')),
    url(r'^admin/', admin.site.urls),
]
