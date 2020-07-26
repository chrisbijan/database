from django.urls import path
from . import views


urlpatterns = [
    path('', views.nickel, name='nickelammonia')
]
