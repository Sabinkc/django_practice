from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("sabin/",views.sabin, name="sabin" ),
    path("renderhtml/", views.renderhtml, name="renderhtml"),
    path("<str:name>",views.greet, name="greet"),
  
]