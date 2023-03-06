from django.urls import path
from polls import views

urlpatterns = [
    path("klk", views.index, name='index')
]