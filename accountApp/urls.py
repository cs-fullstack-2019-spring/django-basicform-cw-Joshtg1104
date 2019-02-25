from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("helloMate/", views.helloMate, name="helloMate"),
    path("add5Dollars/<int:accountID>/", views.add5Dollars, name="add5Dollars"),
]
