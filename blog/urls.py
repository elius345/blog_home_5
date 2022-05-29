from django.urls import path, include
from . import views
#from .views import views
urlpatterns = [
    path('', views.home_view, name="home"),
]
