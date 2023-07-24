from django.urls import path
from . import views

urlpatterns = [
   path("", views.Index.as_view(), name='summa'),
   # path("create/", views.create, name='create')
]