from django.urls import path
from . import views

urlpatterns = [

    path('members/myfirst/', views.myfirst, name='myfirst.html'),

    path('members/profile/', views.profile, name='profile.html'),

    path('members/contact/', views.contact, name='contact.html'),

    path('members/about/', views.about, name='about.html'),
]