from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.main, name='main'),

    path('members/', views.members, name='all_members.html'),

    path('myfirst/', views.myfirst, name='myfirst.html'),

    path('profile/', views.profile, name='profile.html'),

    path('contact/', views.contact, name='contact.html'),

    path('about/', views.about, name='about.html'),

    path('alifmobile', views.alifmobile, name='alifmobile'),
    
    path('alifonline', views.alifonline, name='alifonline'),
    
    path('alifshop', views.alifshop, name='alifshop'),
    
    path('carfinance', views.carfinance, name='carfinance'),
    
    path('deposits', views.deposits, name='deposits'),
    
    path('salam', views.salam, name='salam'),
    
    path('transfers', views.transfers, name='transfers'),

    path('visa', views.visa, name='visa'),
    
    path('members/details/<int:id>', views.details, name='details'),

]