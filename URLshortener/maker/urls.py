from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='maker-home'),
   path('/<str:alias>/', views.redirect, name='maker-redirect')
]
