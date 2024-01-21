from django.urls import path

from .views import show_user,filter_type,hotel_details_form

urlpatterns = [
    path('',show_user),
    path('placedetails/',hotel_details_form),
    path('<str:type>/',filter_type),
]