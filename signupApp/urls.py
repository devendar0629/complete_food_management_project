from django.urls import path

from .views import show_signup_form

urlpatterns = [
    path('',show_signup_form),
]