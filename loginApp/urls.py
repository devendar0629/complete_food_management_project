from django.urls import path,include
from .views import show_login_form

urlpatterns = [
    path('',show_login_form),
]