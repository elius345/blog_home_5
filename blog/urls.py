from django.urls import path, include
#from . import views
from blog import views
urlpatterns = [
    path('', views.home_view, name="home"),
]
