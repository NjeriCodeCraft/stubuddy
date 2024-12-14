from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('study-schedule/', views.study_schedule, name='study-schedule'),
    path('rtl/', views.rtl, name='rtl'),
    path('study-buddy/', views.study_buddy, name='study-buddy'),
    path('virtual-reality/', views.virtual_reality, name='virtual-reality'), 

]