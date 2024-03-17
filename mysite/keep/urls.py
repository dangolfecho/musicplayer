from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path('delete', views.delete, name="delete"),
    path('edit', views.edit, name="edit")
]
