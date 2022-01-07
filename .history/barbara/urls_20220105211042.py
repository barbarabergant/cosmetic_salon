from django.urls import path, re_path
from . import views
from django.utils.translation import gettext_lazy as _
app_name = "barbara"

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('services/', views.services, name='services'),
]