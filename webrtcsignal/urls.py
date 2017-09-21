"""webrtcsignal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import forward
from forward import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^join', views.join),
    url(r'^leave', views.leave),
    url(r'^sdp', views.sdp),
    url(r'^candidate', views.candidate),
    url(r'^get_sdp_candidate', views.get_sdp_and_candidate),
]
