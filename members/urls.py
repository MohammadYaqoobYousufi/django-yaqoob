from django.urls import path
from . import views

urlpatterns = [

    path('members/myfirst/', views.myfirst, name='myfirst.html'),

    path('members/profile/', views.profile, name='profile.html'),

    path('members/contact/', views.contact, name='contact.html'),

    path('members/about/', views.about, name='about.html'),

    path('members/alifmobile', views.alifmobile, name='alifmobile'),
    
    path('members/alifonline', views.alifonline, name='alifonline'),
    
    path('members/alifshop', views.alifshop, name='alifshop'),
    
    path('members/carfinance', views.carfinance, name='carfinance'),
    
    path('members/deposits', views.deposits, name='deposits'),
    
    path('members/salam', views.salam, name='salam'),
    
    path('members/transfers', views.transfers, name='transfers'),

    path('members/visa', views.visa, name='visa'),
]